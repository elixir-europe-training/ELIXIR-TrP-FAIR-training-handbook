---
tags:
     - Interoperability
     - File format
     - Reusability
     - Annotation
     - Documentation 
     
---
<!-- Chapter Types of training materials and their features related to the FAIR training -->

## Description

In this chapter, we discuss different types of training material formats and how they can facilitate or hinder their FAIRness. We also discuss the importance of annotating training material with the minimal necessary information and documenting as much as possible (e.g. by providing instructor notes and/or a lesson plan) for stand-alone re-usability. 

!!! info "Learning outcomes"
    **At the end of this chapter you should be able to:**

     1. Identify most popular training material formats/types 
     2. Identify material types and formats that facilitate interoperability and reusability
     3. Explain the relevance of annotating training material with minimal necessary information for interoperability and  reusability, having a README file, and using naming conventions.
     4. Explain the relevance of documenting (e.g. by providing instructor notes and/or a  lesson plan) for stand-alone re-usability 

## Prerequisites
[Chapter 1](chapter_01.md) 

## Training material formats/types

In Chapter 1, we used a “broad” definition of training materials as anything you would produce yourself (or reuse) as a support for your teaching activity. These can be slides, datasets, videos, software, a GitHub repo, a collection of exercises, Virtual Machines (VMs)/Containers, etc. In summary, any digital object that can be used to deliver a lesson, course, or curriculum. 

Each type of material can be captured in a variety of formats. Each format has advantages and disadvantages in terms of interoperability and (re)usability. Some formats facilitate interoperability, some facilitate (re)usability, some facilitate both. 

!!! example "Exercise"

     Identify possible formats for each type of material. Which format(s) do you mostly adopt? Why?

Table !!!! Add here !!!

!!! example "Exercise"

     Make a list of the most popular formats (according to your experience) and write, for each of them, main advantages and disadvantages in terms of FAIRness.

Table !!!! Add here !!!

!!! example "Exercise"

     Compare the list to Table 1 from the [10 simple rules paper](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1007854#sec007)


## Formats that facilitate interoperability and reusability 

The term interoperability in training materials can be relatively obscure. Still, in this section, we will provide a definition of interoperability for training materials, and we will explain how this concept is related to the idea of reusability. Regarding reusability, it is essential to make a distinction between:
1. Reusing parts of material by repurposing it for a new context or integrating it into another set of materials
2. Reusing the material exactly as it is

File formats will have different implications in the context of FAIRness depending on the two types of material reuse. Some formats facilitate FAIRness while others don’t. To understand which formats facilitate interoperability and reusability, we must first understand these two concepts in the context of training and training materials. 

!!! example "Exercise"

     Read Rule 6 from the 10 simple rules paper, which is mainly about interoperability [10 simple rules paper](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1007854#sec007)

The key point of Rule 6 is: “Training materials need to be captured in interoperable formats, so that they can be used in different contexts (e.g., operating systems and software) and built upon later. For materials like slides, it is important that other trainers are able to (re)use, fine-tune or even extend them. This means that you should choose a format that supports editing and extension. 

Put in simple terms, training material is interoperable when we are able to take parts of it, like slides, exercises, images, etc., and incorporate them in other course material or export it in a different context, as well as fix errors or extend it. This is doable to different extent depending on the material format. Taking parts of a video or modifying a pdf is not impossible, but often requires a licence for the appropriate software or skills not easy to own. Using, e.g., text or markdown files will facilitate the updates of materials or their integration into a new context or a different set of materials. 
Interoperable formats, according to this definition, facilitate the reuse of materials as described in point 1 above. 
Does interoperability always implies reusability? Does a format that supports material editing and extension guarantee that the material can be easily reused? In principle yes, but it is not always the case. 
