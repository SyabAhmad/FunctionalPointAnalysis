# functional Point Analysis
# Sub Topic  Software Engineering (Software Construction and Development)
print("Functional Point Analysis")
print("================================================================")
print("================================================================")
        #Function point metrice
    # provide a standardized method for measuring the various functions
    # of a software application.
        # Allan J. Albrecht initially developed function Point Analysis in 1979 at IBM and it has been further modified by the International Function Point Users Group (IFPUG).
        # FPA is used to make estimate of the software project, including its testing in terms of functionality or function size of the software product.
        # However, functional point analysis may be used for the test estimation
        # of the product. The functional size of the product is measured in terms of
        # the function point, which is a standard of measurement to
        # measure the software application.

# All the parameters mentioned above are assigned
# some weights that have been experimentally determined and are shown in Table
# Weights of 5-FP Attributes

class FunctionsInApplications(object): # class for functions
    def Values(self): # To take those values from user
        NumberOfExternalInputs = 1
        NumberOfExternalOutputs = 2
        NumberOfExternalInquires = 3
        NumberOfInternalFiles = 4
        NumberOfExternalInterfaces = 5

    def WeightingFectorsForSimple(self): # default weights for simple
        NumberOfExternalInputsForSimple = 1
        NumberOfExternalOutputsForSimple = 2
        NumberOfExternalInquiresForSimple = 3
        NumberOfInternalFilesForSimple = 4
        NumberOfExternalInterfacesForSimple = 5
    def WeightingFectorsForAverage(self): # default weights for average
        NumberOfExternalInputsForAverage = 1
        NumberOfExternalOutputsForAverage = 2
        NumberOfExternalInquiresForAverage = 3
        NumberOfInternalFilesForAverage = 4
        NumberOfExternalInterfacesForAverage = 5
    def WeightingFectorsForComplix(self): # default weights for complex
        NumberOfExternalInputsForComplix = 1
        NumberOfExternalOutputsForComplix = 2
        NumberOfExternalInquiresForComplix = 3
        NumberOfInternalFilesForComplix = 4
        NumberOfExternalInterfacesForComplix = 5





