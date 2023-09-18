'''
Each bin has a size of 100 units
Different sizes of items within the same bin are seperated by "!" but each bin 
is seperated by "#" 
if the size of the items within one bin exceeds 100 it is invalid
'''

import sys
import argparse
import flask
import json

app = flask.Flask(__name__)

binPackingInstances = {}
binPackingInstancesCompleted = {}
lastProblemID = 0

def createNewProblem():
    global lastProblemID
    lastProblemID += 1
    problemID = lastProblemID
    binEncoding = ""
    binPackingInstances[problemID] = binEncoding
    binPackingInstancesCompleted[problemID] = False
    return problemID, binEncoding




@app.route('/')
def main():
    return 'Hello and Welcome to Bin Packing.'

@app.route('/newproblem', methods=['GET'])
def newProblem():
    '''
    Input: There is no input for this API endpoint
    Output is a JSON Object: { 'ID': problemID 'bins' : binEncoding }
    The problemID should be an integer that can be used to reference a particular set of bins that are being packed.
    The binEncoding for a new (fresh) instance of bin packing should be an empty set containing no bins
    '''

    problemID, binEncoding = createNewProblem()

    response = {
        "ID": problemID, 'bins': binEncoding
    }
    return json.dumps(response)

@app.route('/placeItem/<problemID>/<size>', methods=['GET'])
def placeItem(problemID, size):
    problemID = int(problemID)
    binPlaced = False
    if binPackingInstancesCompleted[problemID] == True:
        return json.dumps({'error': 'Problem ID has already been completed'})
    binEncoding = binPackingInstances[problemID]
    bins = binEncoding.split('#')
    for index, bin in enumerate(bins):
        items = bin.split('!')
        total_size = sum(int(item) for item in items if item)  
        if total_size + int(size) <= 100:
            items.append(size)
            bins[index] = '!'.join(items)
            new_bin_encoding = '#'.join(bins)
            bin_number = index + 1
            binPlaced = True
            break
    if not binPlaced:
        new_bin_encoding = binEncoding + "#" + str(size)
        bin_number = len(bins) + 1
    binPackingInstances[problemID] = new_bin_encoding
    response = {
        "ID": problemID, 'size': size, 'loc': bin_number, 'bins': new_bin_encoding
    }
    return json.dumps(response)


@app.route('/endproblem/<problemID>', methods=['GET'])
def endProblem(problemID):
    problemID = int(problemID)
    binEncoding = binPackingInstances[problemID]
    bins = binEncoding.split('#')
    total_size = num_items = wasted_space = 0
    num_bins = len(bins)
    binPackingInstancesCompleted[problemID] = True
    for bin in bins:
        items = bin.split('!')
        for item in items:
            total_size += int(item)
            num_items += 1
    
    response = {
        'ID': problemID, 'size': total_size, 'items': num_items, 'count': num_bins, 'wasted' : wasted_space, 'bins' : binEncoding
    }
    return json.dumps(response)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run the bin packing API')
    parser.add_argument('--port', dest='port', type=int, default=5555, help='The port to run the API on')
    parser.add_argument('--host', dest='host', type=str, default='localhost', help='The host to run the API on')
    arguments = parser.parse_args()
    app.run(host=arguments.host, port=arguments.port)