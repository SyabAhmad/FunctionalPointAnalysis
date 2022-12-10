# FunctionalPointAnalysis
FunctionalPointAnalysis


Function point metrics provide a standardized method for measuring the various functions of a software application.
![image](https://user-images.githubusercontent.com/81256221/206850541-da4cd906-ee6e-421a-b059-79b2beb29b0d.png)

Functional Point (FP) Analysis![image](https://user-images.githubusercontent.com/81256221/206850553-d83ad517-fc17-42d3-9d4c-81c5644b162e.png)
Allan J. Albrecht initially developed function Point Analysis in 1979 at IBM and it has been further modified by the International Function Point Users Group (IFPUG). 
FPA is used to make estimate of the software project, including its testing in terms of functionality or function size of the software product. 
However, functional point analysis may be used for the test estimation of the product. The functional size of the product is measured in terms of the function point, which is a standard of measurement to measure the software application.

![image](https://user-images.githubusercontent.com/81256221/206850559-592f2781-2e7c-4a08-95cb-298d75dee054.png)

Objectives of FPA![image](https://user-images.githubusercontent.com/81256221/206850566-b5de3862-5821-4309-b7c9-71cda95a893e.png)

The basic and primary purpose of the functional point analysis is to measure and provide the software application functional size to the client, customer, and the stakeholder on their request. 

Further, it is used to measure the software project development along with its maintenance, consistently throughout the project irrespective of the tools and the technologies.
![image](https://user-images.githubusercontent.com/81256221/206850573-f9ca634f-c8d2-467c-8500-37b2bc034528.png)


Following are the points regarding FPs![image](https://user-images.githubusercontent.com/81256221/206850577-a1e1bbd6-c0fc-4a69-8a1c-90d5af82109a.png)

1.FPs of an application is found out by counting the number and types of functions used in the applications. Various functions used in an application can be put under five types, as shown in Table
![image](https://user-images.githubusercontent.com/81256221/206850581-c1318be6-3ce8-4606-bdf4-f15e6e425c84.png)

![image](https://user-images.githubusercontent.com/81256221/206850587-e4c7b86b-6505-4591-b5c7-116c7ab677bd.png)

The FPA functional units are shown in Fig:![image](https://user-images.githubusercontent.com/81256221/206850591-d9f5ad06-4339-4af3-883d-6da7234d2ab7.png)

![image](https://user-images.githubusercontent.com/81256221/206850595-7dc183cd-b1f5-45ec-9460-d76fb570ac7f.png)

Following are the points regarding FPs…![image](https://user-images.githubusercontent.com/81256221/206850600-7bfe9a19-92be-4b80-b2e6-716a44952cb1.png)

2. FP characterizes the complexity of the software system and hence can be used to depict the project time and the manpower requirement.
3. The effort required to develop the project depends on what the software does.
4. FP is programming language independent.
5. FP method is used for data processing systems, business systems like information systems.
6. The five parameters mentioned above are also known as information domain characteristics

![image](https://user-images.githubusercontent.com/81256221/206850604-646f5c56-7ba0-4159-a707-54de8c7dab8d.png)

7. All the parameters mentioned above are assigned some weights that have been experimentally determined and are shown in Table
![image](https://user-images.githubusercontent.com/81256221/206850607-7d020c0b-80a8-4840-8060-dc3d63f4c8bd.png)

![image](https://user-images.githubusercontent.com/81256221/206850615-0c1f6bf2-28a0-4f59-a0c9-045b0917d987.png)

functional complexities are multiplied with the corresponding weights against each function![image](https://user-images.githubusercontent.com/81256221/206850618-f18697b3-cbcc-4a8a-ab2b-963038de6f14.png)


![image](https://user-images.githubusercontent.com/81256221/206850624-54b267d3-375c-4c31-ae84-b1f151693b9e.png)


Based on the FP measure of software many other metrics can be computed:![image](https://user-images.githubusercontent.com/81256221/206850629-0b80ac88-5b4b-49e3-b3b1-8c9652e77812.png)

Based on the FP measure of software many other metrics can be computed:
Errors/FP
$/FP.
Defects/FP
Pages of documentation/FP
Errors/PM.
Productivity = FP/PM (effort is measured in person-months).
$/Page of Documentation.

![image](https://user-images.githubusercontent.com/81256221/206850632-557e9e9b-0b24-442c-9c0b-5ac1436b3540.png)

value of ∑(fi)![image](https://user-images.githubusercontent.com/81256221/206850660-1d3ca597-3473-45bf-9454-84b066e8ecfc.png)

∑(fi) is the sum of all 14 questionnaires and show the complexity adjustment value/ factor-CAF (where i ranges from 1 to 14). Usually, a student is provided with the value of ∑(fi)



![image](https://user-images.githubusercontent.com/81256221/206850722-e105218b-fc37-4ccd-9b16-d03508c0db45.png)

💻 Example: Compute the function point, productivity, documentation, cost per function for the following data:![image](https://user-images.githubusercontent.com/81256221/206850727-15c55f06-dea0-4692-8af2-117b2162eca4.png)

Number of user inputs = 24
Number of user outputs = 46
Number of inquiries = 8
Number of files = 4
Number of external interfaces = 2
Effort = 36.9 p-m
Technical documents = 265 pages
User documents = 122 pages
Cost = $7744/ month
Various processing complexity factors are: 4, 1, 0, 3, 3, 5, 4, 4, 3, 3, 2, 2, 4, 5=43


![image](https://user-images.githubusercontent.com/81256221/206850730-c58ba4ae-beaa-4f86-b442-b1747bf60951.png)

Example: Compute the function point, productivity, documentation, cost per function for the following data:![image](https://user-images.githubusercontent.com/81256221/206850725-dfce6478-91f6-4d3f-874a-a3559a584287.png)

Solution![image](https://user-images.githubusercontent.com/81256221/206850740-56b554e8-162a-4828-b448-4fdd3b458568.png)
![image](https://user-images.githubusercontent.com/81256221/206850745-9e0b8ac5-a7f2-4c85-a84b-00114101d2b6.png)

Compute the function point, productivity, documentation, cost per function![image](https://user-images.githubusercontent.com/81256221/206850750-397c7c1e-9996-4cff-b122-42db8ee8a109.png)

Functional Point = Count-total * [0.65 + 0.01 *∑(fi)]                                 = 378 * [0.65 + 0.01 * 43]                                 = 378 * [0.65 + 0.43]                                  = 378 * 1.08 = 408

Productivity=FP/EFFORT
=408/36.9=11.1
Total pages of documentation = technical document + user document = 265 + 122 = 387pages

Documentation = Pages of documentation/FP                = 387/408 = 0.94
COST PER FUNTION=Cost / Productivity
=7744/11.1
=$700
![image](https://user-images.githubusercontent.com/81256221/206850752-596464e7-4552-484f-a683-669d1c40fbdd.png)


