# About application
> Checklistfinder is a program that I used at work. Its main task is to find unique numbers and sort pages by key in a PDF file. The program speeds up and makes my work easier when I am putting checklists on the devices. 

<p>
  <img src="https://github.com/xNykram/checklist_finder/blob/master/assets/project2.PNG">
</p>

# Issue description
> The devices are placed randomly during import, which makes my work difficult. When the checklists are printed, my task is to arrange the appropriate lists for the devices. When generating a PDF file with checklists, I am not able to generate the way the devices are arranged (they are unfolded using undefined key).

# Application functions
> The software reads from reqlist.txt all the requests on which it will operate, the list is sorted against the import of devices. Then the program analyzes the PDF and checks if each request from reqlist.txt matches it in PDF. When the program finds out that everything works, it goes to sorting. A new PDF file is created, to which pages taken previously from the PDF file that was generated are added. The pages are of course sorted in the same order as in reqlist.txt. At the very end, the program closes and we get the finished PDF file, which is sorted against the import. After printing, you can spread out the checklists very quickly without wasting a few hours on searching also if there are over 100 devices.

# Summary
>  My project eliminated one of the biggest problems the in company. I received a recommendation from my manager for creating a program and speeding up the process of printing checklists in project.