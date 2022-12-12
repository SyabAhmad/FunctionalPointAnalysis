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

# class FunctionsInApplications(): # class for functions
    # def WeightingFactorsForSimple(self): # default weights for simple
    # simpleWeightingFactors = {7, 5, 3, 4, 3}
    # AverageWeightingFactors = {4, 4, 6, 10, 5}
    # ComplexWeightingFactors = {15, 10, 6, 7, 6}
        # NumberOfExternalInputsForSimple = 7
        # NumberOfExternalOutputsForSimple = 5
        # NumberOfExternalInquiresForSimple = 3
        # NumberOfInternalFilesForSimple = 4
        # NumberOfExternalInterfacesForSimple = 3
    # # def WeightingFactorsForAverage(self): # default weights for average
    #     NumberOfExternalInputsForAverage = 4
    #     NumberOfExternalOutputsForAverage = 4
    #     NumberOfExternalInquiresForAverage = 6
    #     NumberOfInternalFilesForAverage = 10
    #     NumberOfExternalInterfacesForAverage = 5
    # # def WeightingFactorsForComplix(self): # default weights for complex
    #     NumberOfExternalInputsForComplix = 15
    #     NumberOfExternalOutputsForComplix = 10
    #     NumberOfExternalInquiresForComplix = 6
    #     NumberOfInternalFilesForComplix = 7
    #     NumberOfExternalInterfacesForComplix = 6


class ForSimpleWeights:
    #
    def SimpleManagerPanel(self):
        AllQuestionaries = 43
        simpleWeightingFactors = [7, 5, 3, 4, 3]
        NumberOfExternalInputs = int(input("Number Of External Inputs: "))
        NumberOfExternalOutputs = int(input("Number Of External Outputs: "))
        NumberOfExternalInquires = int(input("Number Of External Inquires: "))
        NumberOfInternalFiles = int(input("Number Of Internal Files: "))
        NumberOfExternalInterfaces = int(input("Number Of External Interfaces: "))
        TotalCount = (NumberOfExternalInputs*simpleWeightingFactors[0])+(NumberOfExternalOutputs*simpleWeightingFactors[1])+(NumberOfExternalInquires*simpleWeightingFactors[2])+(NumberOfInternalFiles*simpleWeightingFactors[3])+(NumberOfExternalInterfaces*simpleWeightingFactors[4])
        print("**=======================**")
        print("**=======================**")
        print("Total Count = " , TotalCount)
        print("**=======================**")
        FunctionPoint = TotalCount*(0.65+0.01*AllQuestionaries)
        print("Functional Point = ", FunctionPoint )
        print("**=======================**")
        print("**=======================**")

        Effort = float(input("To Find Productivity  Enter Total Effort"))
        Productivity = FunctionPoint/Effort
        print("Productivity = ", Productivity)
        print("**=======================**")
        print("**=======================**")


        print("To Find Total Documentation (Pages): ")
        UserDocumantaion = int(input("Enter User Documentation (Pages): "))
        TechnicalDocumentation = int(input("Enter Technical Documentation (Pages): "))
        TotalDocumantaion = UserDocumantaion+TechnicalDocumentation
        print("Total Pages= ", TotalDocumantaion)
        print("**=======================**")
        print("**=======================**")


        Documantaion = TotalDocumantaion/FunctionPoint
        print("Documentation = ", Documantaion)
        print("**=======================**")
        print("**=======================**")


        print("To Find Cost per Function: ")
        TotalCost = float(input("Enter Cost: "))
        CostPerFunction = TotalCost/Productivity
        print("Cost per Function = ", CostPerFunction)
        print("**=======================**")
        print("**=======================**")



class ForAverageWeights:
    #
    def AverageManagerPanel(self):
        AllQuestionaries = 43
        AverageWeightingFactors = [4, 4, 6, 10, 5]
        #Functions = FunctionsInApplications()
        NumberOfExternalInputs = int(input("Number Of External Inputs: "))
        NumberOfExternalOutputs = int(input("Number Of External Outputs: "))
        NumberOfExternalInquires = int(input("Number Of External Inquires: "))
        NumberOfInternalFiles = int(input("Number Of Internal Files: "))
        NumberOfExternalInterfaces = int(input("Number Of External Interfaces: "))
        TotalCount = (NumberOfExternalInputs * AverageWeightingFactors[0]) + (NumberOfExternalOutputs * AverageWeightingFactors[1]) + (NumberOfExternalInquires * AverageWeightingFactors[2]) + (NumberOfInternalFiles * AverageWeightingFactors[3]) + (NumberOfExternalInterfaces * AverageWeightingFactors[4])
        print("**=======================**")
        print("**=======================**")
        print("Total Count = ", TotalCount)
        print("**=======================**")
        FunctionPoint = TotalCount*(0.65+0.01*AllQuestionaries)
        print("Functional Point = ", FunctionPoint)
        print("**=======================**")
        print("**=======================**")

        Effort = float(input("To Find Productivity  Enter Total Effort"))
        Productivity = FunctionPoint / Effort
        print("Productivity = ", Productivity)
        print("**=======================**")
        print("**=======================**")

        print("To Find Total Documentation (Pages): ")
        UserDocumantaion = int(input("Enter User Documentation (Pages): "))
        TechnicalDocumentation = int(input("Enter Technical Documentation (Pages): "))
        TotalDocumantaion = UserDocumantaion + TechnicalDocumentation
        print("Total Pages = ", TotalDocumantaion)
        print("**=======================**")
        print("**=======================**")

        Documantaion = TotalDocumantaion / FunctionPoint
        print("Documentation= ", Documantaion)
        print("**=======================**")
        print("**=======================**")


        print("To Find Cost per Function: ")
        TotalCost = float(input("Enter Cost: "))
        CostPerFunction = TotalCost / Productivity
        print("Cost per Function = ", CostPerFunction)
        print("**=======================**")
        print("**=======================**")

class ForComplexWeights:
    #
    def ComplexManagerPanel(self):
        AllQuestionaries = 43
        ComplexWeightingFactors = [15, 10, 6, 7, 6]
        # Functions = FunctionsInApplications()
        NumberOfExternalInputs = int(input("Number Of External Inputs: "))
        NumberOfExternalOutputs = int(input("Number Of External Outputs: "))
        NumberOfExternalInquires = int(input("Number Of External Inquires: "))
        NumberOfInternalFiles = int(input("Number Of Internal Files: "))
        NumberOfExternalInterfaces = int(input("Number Of External Interfaces: "))
        TotalCount = (NumberOfExternalInputs * ComplexWeightingFactors[0]) + (
                    NumberOfExternalOutputs * ComplexWeightingFactors[1]) + (
                                 NumberOfExternalInquires * ComplexWeightingFactors[2]) + (
                                 NumberOfInternalFiles * ComplexWeightingFactors[3]) + (
                                 NumberOfExternalInterfaces * ComplexWeightingFactors[4])
        print("**=======================**")
        print("**=======================**")
        print("Total Count = ", TotalCount)
        print("**=======================**")
        print("**=======================**")


        FunctionPoint = TotalCount * (0.65 + 0.01 * AllQuestionaries)
        print("Functional Point = ", FunctionPoint)
        print("**=======================**")
        print("**=======================**")

        Effort = float(input("To Find Productivity  Enter Total Effort"))
        Productivity = FunctionPoint / Effort
        print("Productivity = ", Productivity)
        print("**=======================**")
        print("**=======================**")

        print("To Find Total Documentation (Pages): ")
        UserDocumantaion = int(input("Enter User  (Pages): "))
        TechnicalDocumentation = int(input("Enter Technical Documentation (Pages): "))
        TotalDocumantaion = UserDocumantaion + TechnicalDocumentation
        print("Total Pages= ", TotalDocumantaion)
        print("**=======================**")
        print("**=======================**")

        Documantaion = TotalDocumantaion / FunctionPoint
        print("Documentation= ", Documantaion)
        print("**=======================**")
        print("**=======================**")


        print("To Find Cost per Function: ")
        TotalCost = float(input("Enter Cost: "))
        CostPerFunction = TotalCost / Productivity
        print("Cost per Function = ", CostPerFunction)
        print("**=======================**")
        print("**=======================**")
class ControlPanel:
    def ControlPanelManager(self):
        SimpleManager = ForSimpleWeights()
        AverageManager = ForAverageWeights()
        ComplexManeger = ForComplexWeights()
        print("Function Point Analysis")
        print("1: weighting Factor for \"Simple\" ")
        print("2: weighting Factor for \"Average\" ")
        print("3: weighting Factor for \"Complex\" ")

        optionChoice = int(input("Enter Your Desire Input"))

        if optionChoice == 1:
            SimpleManager.SimpleManagerPanel()
        elif optionChoice == 2:
            AverageManager.AverageManagerPanel()
        elif optionChoice == 3:
            ComplexManeger.ComplexManagerPanel()
        else:
            print("Invalid Arguments")






ControlManager = ControlPanel()
ControlManager.ControlPanelManager()