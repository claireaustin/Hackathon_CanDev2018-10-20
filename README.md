### [CANDEV Data Challenge](https://www.statcan.gc.ca/eng/candev/index)
##### Statistics Canada in collaboration with the University of Ottawa, October 20-21, 2018
##### University of Ottawa, [Learning Crossroads Building](https://www.uottawa.ca/facilities/learning-crossroads), 100 Louis-Pasteur Private [map](https://www.google.com/search?q=map+100+louis+pasteur+ottawa&ie=utf-8&oe=utf-8&client=firefox-b-ab)
# Business case: "Automating data fitness assessment"

## Table of Contents
* [Business Issue](#business-issue)  
* [Background Material](#background-material)
* [What will you need](#what-will-you-need)
* [Tasks](#tasks)
* [Deliverables](#deliverables)
* [Key points to remember](#key-points-to-remember)

### Business Issue
At [Environment and Climate Change Canada][link_ECCC], we would like to address the problem of assessing data fitness for use. The aim is to automate the assessment of diverse datasets against specified criteria and to programmatically generate a report on the results of the assessment. The ultimate objective is policy development that enables improved data governance and data management.

### Background Material
Big Data has the potential to answer questions, provide new previously inaccessible insights, and strengthen evidence-informed decision making. However, the harnessing of Big Data can also very easily overwhelm existing resources and approaches, keeping those answers and insights out of reach.

Many organizations are faced with inconsistent data quality and uncontrolled data flow pathways. This situation presents people at the working level and upper management alike with enormous challenges in developing and implementing solutions for Big Data, and policies for data governance and data publication. 

It is widely recognized that a major hurdle for analysts and data scientists is data preparation which can take up to 70% or more of the total time spent on data analysis, essentially performing tasks left undone when data providers release data that are not [FAIR](https://www.force11.org/group/fairgroup/fairprinciples) (Findable, Accessible, Interoperable, and Reusable).

If data stewards and repositories had an automated tool to check if data meet certain specified criteria, an organization could implement efficient and effective controls in the data workflow. The result would be improved data management and quality, less time spent on data preparation, reduction or elimination of inefficiencies and costly errors, and a reduction in the costs associated with getting better answers more quickly from Big Data and artificial intelligence (AI). 

Today we will ask you to build a tool to automate checking datasets against criteria specified in provided data checklists. 

### What you will need
* Data checklist modules [Repository][link_DGRRepo].
* [Preprint][link_preprint] "A path to Big Data readiness" for background and description of the data checklists.
* A modified version of the Ocean Health Index (OHI) data.<sup>1</sup>
* OHI [data][link_OHIData] (modified with errors introduced).
* OHI [metadata][link_metadata].
* OHI [background][link_OHIbackground].

### Tasks
1. Build a tool to assess the modified OHI data against **Module 2b (data format/structure)** from the Big data readiness checklists.
2. Develop an overall pass/fail dataset rating based on assessment results to conclude if the dataset(s) is/are reuseable or not.
3. Produce an R markdown report containing at least:
    * Overview or summary of the assessment results.
    * Detailed assessment results.
   #### Optional (*in addition* to the above):
4. Add one or more modules from the Big data readiness checklists to your tool (in addition to module 2b). 
5. Process any other publicly available dataset of your choosing. If you do this, you must process these data against module 2b and against any of the optional modules that you selected in Step 4.

### Deliverables
1. A PowerPoint presentation demonstrating implementation of the tool(s) developed.
2. Your R markdown report (code and PDF output).
3. All your computer code.
4. All your deliverables deposited in a GitHub public repository with a [GNU General Public Licence version 3](https://opensource.org/licenses/GPL-3.0). 

### Key points to remember
* Use only free, open source software.
* All implementation must be based on original work.
* Provide appropriate attributions and hyperlinks in your deliverables.

1. Ocean Health Index. 2018. ohi-global version: Global scenarios data for Ocean Health Index, [10-18-2018]. National Center for Ecological Analysis and Synthesis, University of California, Santa Barbara. Available at: https://github.com/OHI-Science/ohi-global/releases
  
  [link_ECCC]:https://www.canada.ca/en/environment-climate-change.html
  [link_DGRRepo]:https://t2m.io/X4P3cXI4  
  [link_OHIData]:https://github.com/claireaustin/Hackathon_CanDev2018-10-20/blob/master/OHIDataSet.csv
  [link_OHIbackground]:http://ohi-science.org/news/Biography-OHI
  [link_metadata]:https://github.com/OHI-Science/ohi-global/tree/draft/global2017#ohi-2017-global-metadata
  [link_preprint]:https://github.com/claireaustin/BigDataReadiness/blob/master/Austin2018PREPRINT_PathToBigDataReadiness.pdf
  

