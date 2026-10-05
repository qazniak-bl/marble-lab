# jse-mechanics-template
### D Evangelista, 2026





## Should I use this template?

Use this template if you are preparing an article for submission to [Journal of Science & Engineering](https://j.snerds.org) **in the area of physics/mechanics**. Do not use this template if your article is in electricity and magnetism (use the IEEE template), or for senior project or Hackathon abstracts. Articles in the areas of computer science, chemistry, biology, advanced mathematics, or other are still TBD but will likely use some other appropriate journal formatting. 



## Using github

We recommend you clone and fork this github repository as a starting point. Keep your initial submission PDF and comments received in the initial directory. Keep your revised PDf, response to reviewer, etc in the revised section. The actual revisions themselves are kept in the git revision history. **Preparing an outline and having a full git revision history in which you edit and respond to reviewer comments is one way you can show the work is your own and not that of an AI. If you keep your data in this same repository you are also making your data and analyses transparent and replicable.**




## General guidance

  * Do not waste time formatting it to look like a journal as you will likely do it wrong and it will have to be put into Latex anyway.
  * Do not waste time trying to get figures into the “right” place. It’s OK if they’re even separate files because you will likely do it wrong getting text to wrap around the figure in your Google Doc and it will have to be redone in Latex anyway.
  * **Do not add junk to make it longer.** You’re not graded on page count. Longer page count will be penalized or rejected.
  * Do consider starting with an outline to show the editor that you, and not an AI, actually wrote this. Keeping your drafts in a Github repository so I can see the revision history is also sufficient to help establish this was not done by an AI.
  * **Remember to provide AI spot check results in your submission**
  * Remember to give an informative title
  * Authors can be listed in any order you like. Normally the first author is thought of as a special position. Also the corresponding author is a special position. The last author is normally the research advisor or most senior person on the list. 




## Required sections

In addition to the sections below, you must provide an informative title! 

    I. Abstract – one paragraph only, normally has no references
    II. Introduction – work from broad to specific. Give major important background information or set up the major concepts to be used or tested. Set up the key research questions or hypotheses to tested. Optionally, give top level overview of method to be used. This section also acts as a literature review of other important work in the field and relevant to the questions at hand.  Equations are appropriate here if needed; symbols should be consistent throughout the paper. Remember in science we do not “prove” hypotheses, we can disprove alternatives by falsifying them, and that any hypotheses we propose must be testable (as in there must be a way to show it was wrong). 
    III. Methods and materials – Provide all methods and materials in a form that is replicable by a competent scientist or engineer. This section is normally written in past tense, e.g. “We used an Easy Bake Oven (Hasbro; Pawtucket, RI) to evaporate plutonium samples to complete dryness…” 
        A. Consider breaking the methods into subsections, either for different major methods or parts of the experiment
        B. Alternatively you could break it down into subsections based on things like… experimental subjects… testing… statistical analyses, etc. Major models or equations are appropriate here if they explain how you are handling your data. 
        C. Do not include results in your methods. The methods tell other scientists how to replicate what you did. Do not provide a laundry list or recipe of steps like you copied from a lab handout or an AI; these will be rejected. 
        D. It is appropriate to put links to code or datasets; put long items in an appendix or provide online. 
    IV. Results – The results should deal with “just the facts” exactly what you saw or measured, without interpretation. You should include graphs, tables, summary statistics, and results of statistical tests here. The key thing here is that you are reporting truthfully what you saw as just the facts; people may differ on the interpretations but results ought to be taken at face value unless your methods are flawed. Figures and tables must be numbered and must be referred to in the text. 
    V. Discussion – The discussion is where you interpret the meaning of your results and whether they support your hypotheses or refute alternative hypotheses. You should refer to tables, figures, etc by number and use them in supporting your arguments here. 
    VI. Acknowledgements – Keep it short or the editors will shorten it for you. 
    VII. References – Do not spend too much time trying to perfectly format per MLA or whatever because journals often have their own preferred formats; as long as you have author, title, journal, year, volume, page number it will be findable. Peer reviewed journals or published work only; Food Girl’s Blog is not a peer reviewed journal; Wikipedia is not a peer reviewed journal; Webster’s Dictionary is not necessary in a scientific journal article. If I find fake references your paper will be rejected. 




## Figures

**Figures should be formatted for 1 column width which is 3.4167 inches or 246 point.** Your figure should be relevant to the text, easily readable, not distracting. You must provide a **caption for each figure**, and **each figure must be referred to in the text by number** (e.g. Fig 2 shows the third Zonklar moment as a function of t). 

### Vector art
**Vector art**, like graphs and diagrams you drew, should be done as a SVG in something like Inkscape (free) or Adobe Illustrator. These vector formats are scalable, which is why you use them here. Do not do these as a JPG or PNG as those formats become pixellated if you zoom them in or out. 

### Raster art
**Raster art** like photos or scientific illustrations, paintings, drawings, should be done at 600 dpi or higher, as a raster format like JPG PNG etc. **Please provide the original raw files** (not with text overlays) so they can be properly compsed into the figure using Inkscape. Please provide the original images in as high a resolution as is available. **Image manipulation is bad** is manipulating data and should not be done. Image adjustment to crop, etc is OK and ought to typically done in something like Adobe Photoshop or Gimp (free).

### Graphs
If you do the graphs in Python matplotlib or R provide the raw data in csv or other text based form and provide the code used to generate the graph. These packages can output SVG or PNG as needed, and are preferred. 

**Do not include titles on your graphs or images**; it's more work for me to strip them out. Titles for such things are normally contained in the caption for the figure which you should provide either as a text file or in your manuscript text - do not put it on the image!




## Tables
Tables are typically prepared in Latex using the `table` and `tabular` environments. If you cannot write Latex tables then provide the raw data in .csv or .xlsx format; **one file per table with just the numbers and text that are to be in the table**. 

As with figures, **every table should have a caption and should be referred to in the text by number.** 




## Cross references
To save time J S&E uses the built-in Latex cross referencing mechanisms (`\label{labelname}` and `\ref{labelname}`) as well as the Latex [Cleveref package](https://ctan.org/pkg/cleveref?lang=en) commands (`\cref{labelname}` and related) to automagically handle cross referencing. Follow the examples as given in example file or you will make the editor grumpy. 




## References
J S&E uses bibtex to handle reference formatting. If you are unable to do bibtex following the example .bib file, then provide your references such that you are including the following (at minimum):

 * For published peer reviewed journal articles give author, year, title, journal, volume, and page; DOI if available
 * For books, give author, year, title, publisher, ISBN if available
 * Software packages often have instructions for how to cite them; follow those instructions
 * Do not cite junk material. No blogs, no pop websites, no Wikipedia. 
 * **Fake citations will cause your article to be rejected**
 
References are checked when accepted articles are sent to Crossref for indexing. 


## AI check
You are required to do spot checks for AI and plagiarism and submit those as part of your initial submission. Reviewers and the editor will also check. Your submissions are also checked with a plagiarism and AI detector. **If you submit AI or plagiarized work your article may be rejected and/or disciplinary action may be taken.** By showing a continuous chain from initial outlines, drafts, etc through a Github history, as well as revisions and comments and responses to reviewers you help to establish the work as your own and also make the science more transparent.  
 
