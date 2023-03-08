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

| Formats | Interoperability | Reusability |
| --- | --- | --- |
| pdf | partially | yes | 
| | *A pdf can be read in any OS, but to modify it you need to pay a licence* | *Only as is* | 
| | *Explanation* | *Explanation* | 
| | yes/no/partially | yes/no/partially | 
| | *Explanation* | *Explanation* | 


!!! example "Exercise"

     Make a list of the most popular formats (according to your experience) and write, for each of them, main advantages and disadvantages in terms of FAIRness.

Table !!!! Add here !!!

!!! example "Exercise"

     Compare the list to Table 1 from the [10 simple rules paper](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1007854#sec007).


## Formats that facilitate interoperability and reusability 

The term interoperability in training materials can be relatively obscure. Still, in this section, we will provide a definition of interoperability for training materials, and we will explain how this concept is related to the idea of reusability. Regarding reusability, it is essential to make a distinction between:
     1. Reusing parts of material by repurposing it for a new context or integrating it into another set of materials
     2. Reusing the material exactly as it is

File formats will have different implications in the context of FAIRness depending on the two types of material reuse. Some formats facilitate FAIRness while others don’t. To understand which formats facilitate interoperability and reusability, we must first understand these two concepts in the context of training and training materials. 

!!! example "Exercise"

     Read Rule 6 from the 10 simple rules paper, which is mainly about interoperability [10 simple rules paper](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1007854#sec007).

The key point of Rule 6 is: “Training materials need to be captured in interoperable formats, so that they can be used in different contexts (e.g., operating systems and software) and built upon later. For materials like slides, it is important that other trainers are able to (re)use, fine-tune or even extend them. This means that you should choose a format that supports editing and extension. 

Put in simple terms, training material is interoperable when we are able to take parts of it, like slides, exercises, images, etc., and incorporate them in other course material or export it in a different context, as well as fix errors or extend it. This is doable to different extent depending on the material format. Taking parts of a video or modifying a pdf is not impossible, but often requires a licence for the appropriate software or skills not easy to own. Using, e.g., text or markdown files will facilitate the updates of materials or their integration into a new context or a different set of materials. Interoperable formats, according to this definition, facilitate the reuse of materials as described in point 1 above. 

Does interoperability always implies reusability? Does a format that supports material editing and extension guarantee that the material can be easily reused? In principle yes, but it is not always the case. 

!!! example "Exercise"

     Have a look at the slides on the [String Database (by Lars Juhl Jensen)](https://www.slideshare.net/larsjuhljensen/the-string-database) on Slideshare. Imagine the slides were downloadable in pptx format. 
     1. Could the presentation be extended?
     2. Could you choose a few slides and incorporate them in your presentation?
     3. Could you easily fix a typo?
     
If you answered yes to the three questions above, it is likely that the String Database materials are interoperable, but not necessarily easy to reuse (see the next session). 

However, what if the presentation was in pdf? Unless you had a licence allowing you to modify pdf files, the only way to reuse the presentation would be to reuse it exactly as it is. 

!!! example "Exercise"

     Consider the list in table 2. For each format, specify whether it is interoperable, reusable or both and explain the reason for your opinion. 
     
     | Formats | Interoperability | Reusability |
     | --- | --- | --- |
     | pdf | partially | yes | 
     | | *A pdf can be read in any OS, but to modify it you need to pay a licence* | *Only as is* | 
     | | *Explanation* | *Explanation* | 
     | | yes/no/partially | yes/no/partially | 
     | | *Explanation* | *Explanation* | 

## Documenting training materials for stand-alone re-usability

Reconsider the slides about the [String Database (by Lars Juhl Jensen)](https://www.slideshare.net/larsjuhljensen/the-string-database) on Slideshare that we have seen above. Would it be straightforward to reuse the String Database presentation as stand-alone material? Each slide contains a single word or a short sentence. For example, here  is the content of the first 10 slides:
     1. Introduction to STRING Lars Juhl Jensen EMBL Heidelberg
     2. STRING
     3. integrate diverse evidence
     4. functional interactions
     6. hundreds of proteomes
     7. Ensembl
     8. SWISS-PROT
     9. prokaryotes
     10. genomic context methods

How do you imagine a trainer teaching over these slides? What narrative would you use if you were to teach it? How could you find it out? Going further, these slides can be in Zenodo, have a DOI, have metadata describing it, be linked to TeSS, and still, you would not be able to teach if you don’t have at least some indication of what you should say because the slides do not have some narrative.
Thus there are two orders of problems: one is related to the format (see previous session), the other to the content and/or additional information provided with the material and explaining its purpose, how the material should be used (for self-learning, in classroom teaching) and delivered (mode of delivery). Interoperable formats are often reusable (e.g., pptx, markdown), but the reverse is only sometimes true. Some formats allow reuse of material while not being interoperable. In these cases, the material can only be reused as is and cannot be easily modified. Examples are pdf, png, jpeg, etc. formats. 

When training material is provided in reusable but not interoperable format, which means it should be used as is, it is particularly important that it is accompanied by some documentation explaining how the material is to be used, including - when appropriate - an extensive narrative describing word-by-word the meaning and purpose of each, e.g.,  slide or exercise.

There are a few effective ways to do this:
     - For a lecture-style presentation, you can annotate each slide with an extensive narrative capturing all aspects of the subject on the slides. You can put the complete transcript of the verbal presentation in the Notes panel in Powerpoint or in Google slides. Suppose you want to share your slides in pdf format. In that case, it is handier to place the detailed content into a handbook or use text-book style reference materials and keep the slides for lectures cleaner, only placing relevant elements directly on the slides. 
     - You may create a lesson plan describing the purpose and the mode of delivery of each piece of material. Lesson plans could contain many practical details, including - for each part of the material - the time needed for the delivery, the learning experiences and expected learning outcomes. 
     - You may associate “Instructor notes” with the materials, but you don’t need to include them in the materials. The Instructor notes should provide information drawing on your experience or the experience of other instructors. They may consist of technical tips and tricks, common problems, and a description of what parts or exercises are essential and what could be skipped in case of lack of time. 

 Documenting training materials makes training materials easily reusable not only by other trainers but also by yourself in the future. It is an excellent practice for any material, especially when it is not self-explanatory like the slides described above ([String Database (by Lars Juhl Jensen)](https://www.slideshare.net/larsjuhljensen/the-string-database)).
 
 > "The secret to good documentation is to write it while you're writing the code. You are your first audience. Explain what you're doing to yourself. Future you will thank you!" — *Victoria Drake November 24, 2020* –

!!! example "Exercise"

     Reflect on the following:
     - How do you document your training material?
     - What other option do you know?
     
!!! example "Exercise"

     - Think about the following types/formats: pptx, pdf, png, md (on GitHub), VM/Container
     - How would you document materials in each of these types/formats?



