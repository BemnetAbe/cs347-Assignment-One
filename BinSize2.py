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

@app.route('/placeitem/problemID/size', methods=['POST'])
def placeItem():
# The problemID should be the same as was provided in the input

# new_item_size should be the size of the newly placed item

# bin_number should be the number of the bin where the new item was placed. (Please number the first bin as 1)

# The new_bin_encoding should be a string encoding the set of bins with the new itemed placed.

# Multiple bins with its own ID that could have multiple bins that could be worked
def endProblem():


