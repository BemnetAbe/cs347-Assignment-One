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
lastProblemID = 0

def createNewProblem():
    global lastProblemID
    lastProblemID += 1
    problemID = lastProblemID
    binEncoding = []
    binPackingInstances[problemID] = binEncoding
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
    binEncoding = binPackingInstances[problemID]
    bins = binEncoding.split('#')
    binPlaced = False
    for index, bin in enumerate(bins):
        items = bin.split('!')
        total_size = 0
        for item in items:
            total_size += int(item)
        if total_size + int(size) <= 100:
            new_bin_encoding = binEncoding.replace(bin, bin + '!' + size)
            bin_number = index + 1
            binPlaced = True
            break
    new_item_size = size
    if not binPlaced:
        if binEncoding == "":
            new_bin_encoding = str(new_item_size) + "#"
        else:
            new_bin_encoding = binEncoding + "#" + str(new_item_size)
        bin_number = len(bins) + 1
    response = {
        "ID": problemID, 'size': new_item_size, 'loc': bin_number, 'bins': new_bin_encoding
    }
    return json.dumps(response)

@app.route('/endproblem/<problemID>', methods=['GET'])
def endProblem(problemID):


