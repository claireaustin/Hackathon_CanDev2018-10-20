# CANDEV Hackathon
## Automating data fitness

## Table of Contents
* [Business Issue](#business-issue)  
* [Background Material](#background-material)
* [What will you need](#what-will-you-need)
* [Tasks](#tasks)
* [Key points to remember](#key-points-to-remember)

### Business Issue
At Environment and Climate Change Canada, we would like to address the problem of assessing data fitness for use. The aim is to automate the assessment of diverse datasets against specified criteria and to programmatically generate a report on the results of the assessment. The ultimate objective is policy development that enables improved data governance and data management.

### Background Material
Big Data has the potential to answer questions, provide new previously inaccessible insights, and strengthen evidence-informed decision making. However, the harnessing of Big Data can also very easily overwhelm existing resources and approaches, keeping those answers and insights out of reach.

Many organizations are faced with inconsistent data quality and uncontrolled data flow pathways. This situation presents people at the working level and upper management alike with enormous challenges in developing and implementing solutions for Big Data and policies for data governance and data publication. 

It is widely recognized that a major hurdle for analysts and data scientists is data preparation which can take up to 70% or more of the total time spent on data analysis, essentially performing tasks left undone when data providers release data that are not FAIR (Findable, Accessible, Interoperable, and Reusable).

If data stewards and repositories had an automated tool to check if these criteria have indeed been met, an organization could implement efficient and effective controls in the data workflow. The result would be improved data management and quality, less time spent by analysts on data preparation, reduction or elimination of inefficiencies and costly errors, and a reduction in the costs associated with getting better answers more quickly.

Today we will ask you to build a tool to automate checking these criteria using a modified version of the Ocean Health Index (OHI) data<sup>1</sup>. 

### What you will need
* The checklists in Big Data Readiness Checklist [Repo][link_DGRRepo]
* The modified (w/errors introduced) [data][link_OHIData] from the OHI
* [Background][link_OHIbackground] on the OHI
* Link to the OHI [metadata][link_metadata]
* [Preprint][link_preprint] on the background for the checklists

### Tasks
* Build a tool to process the OHI data through **at least** module 2b (data format/structure) from the Big data readiness   checklists 

### Key points to remember
* Use only free, open source software.
* All implementation must be based on original work.

1. Ocean Health Index. Year. ohi-global version: Global scenarios data for Ocean Health Index, [10-18-2018]. National Center for Ecological Analysis and Synthesis, University of California, Santa Barbara. Available at: https://github.com/OHI-Science/ohi-global/releases
  
  [link_DGRRepo]:https://t2m.io/X4P3cXI4  
  [link_OHIData]:https://github.com/claireaustin/Hackathon_CanDev2018-10-20/blob/master/OHIDataSet.csv
  [link_OHIbackground]:http://ohi-science.org/news/Biography-OHI
  [link_metadata]:https://github.com/OHI-Science/ohi-global/tree/draft/global2017#ohi-2017-global-metadata
  [link_preprint]:https://github.com/claireaustin/BigDataReadiness/blob/master/Austin2018PREPRINT_PathToBigDataReadiness.pdf
  

