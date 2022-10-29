# Hash2Hash_Compare.py #

## BETA Version 0.2 UPDATE: ## 

A Simple Python Script to Compare a Set of Hash Values to a Known Reference Library of Hash Values.

Since the original version iterated through each line of the files - it took forever to run through the reference set. (Over 12 hours...just to get a little over halfway!)

I wrote a second python script that broke up the Known Reference Library into 16 separate smaller files organized by the first character of the SHA-1 Hash Value (0 to F).

The original Hash2Hash_Compare.py script was then modified to search against the 16 smaller grouped files, significantly improving the search times.

## How to use this script: ##

Download a set of known hash files... I recommend the National Software Resource Library (NSRL) minimal version. You can read more about them here:

https://www.nist.gov/itl/ssd/software-quality-group/national-software-reference-library-nsrl/nsrl-download/current-rds

Make sure you change the permissions of the python scripts to make them executable:

``` $ sudo chmod +x Hash2Hash_Compare.py ```

``` $ sudo chmod +x Split_Hash_File.py ```

Move or copy the python scripts and reference hash file into the same location and/or folder of your choice.

Next, run the Split_Hash_File.py to split the NSRL reference file into 16 smaller files.

```$ sudo ./Split_Hash_File.py [Path to feference file] ```

Lastly, run the Hash2Hash_Compare.py script:

``` $ ./Hash2Hash_Compare.py [Filename of unknown hashses] [Filename for the report file] ```

## Notes: ##

Thank you to Alexis Brignoni for his willingness to review and work with me on this journey! Check out his work here: https://github.com/abrignoni 

System used: 

- Dell Latitude Laptop with an Intel Core i7-4510U and 12GB of RAM
- Kali Linux 
- Python 3.10.7

Data:

- NSRL RDS Hash Set: https://s3.amazonaws.com/rds.nsrl.nist.gov/RDS/current/rds_modernm.zip
  RDS Version 2.78 - September 2022 - download and verified by the published hash value of the file (094bd298d2ef804558a2276c11c4eb6ea7a3a1b6).
- Data analysis of the original NSRL hash set showed the file has a total of 48,688,686 lines of data.
- After running the python script to split the NSRL hash set the original file was again verified by hash check. (No changes)
- Each of the text files split by the python script were then validated against the original file by line count, diff checks, and then reconstituted into a   single csv file and compared using Libre Office Calc (a spreadsheet editor) where column A was the split data in temporal order and column B was the       original hashes from the hash set. Using the Match function, each line was compared and resulted in a 100% match.  
- The Hash2Hash_Compare.py script was then validated against a small subset of data derived from the NSRL Hash set and fictional hashes.
- The Hash2Hash_Compare.py read, compared, and correctly identified and output the fictional hash values to the report file.
- Using the "time" command the Hash2Hash_Compare.py script was run against a full known set of data. The script succuessfully completed in 323.12 seconds.

Future Plans:

- Optimize for speed by reducing the number of unecessary reads - more targeted specificity of the hashes.
- Testing the binary search functions like "bisect" to see if that increases speed of searches.  

Lessons Learned:

- Indentation matters and can be an extremely frustrating problem to fix.
- Stubborness pays off when continuing to work on the script until it works!
- "break" only works "Inside a Loop" and doesn't work with "if" statements.
- "pass" does work with "if" statements.
