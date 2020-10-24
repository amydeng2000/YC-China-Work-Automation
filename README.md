# YC-China-Work
Code I wrote to automate MiraclePlus' (prev. YC China) workflow

### PR Analysis
* **Context:** The last question on MiraclePlus' application asks founders how they heard about the incubator in order to collect marketing data. The core team wanted the question to be a short free response, thus we need to extract labels from the responses to create a more sturctualized dataset. I wrote this code to automate the labeling process and the statistical analysis. 
* **Design:** The code can be ran on command lines in order for colleagues without coding experience to reuse. It requires users to input the file names and output two .csv files containing the labeled responses and the stats corresponding to the labels. The program outlines all instructions in the command line, checks for errors, and explain errors in simple words for non-tech users. 
* **Deployment:** This program is now used by the PR team to label 2400+ entries


### Web Crawling & Image to Text
* **Context:** MiraclePlus sources extensively from top universities and research institutions in China. We find it very effective to cold email professors and team leads who would have startup projects that qualifies for the incubator. Therefore, we need to scrape researchers emails from the internet in large amounts. This is a web crawler I wrote that scraped 1200+ emails from www.aminer.cn. Since the emails on the website is shown as pictures, OCR is used to read those images to text. 
* **Design:** Inspecting the website shows that the return data is not structured, and the website doesn't allow direct requests. Therefore, I chose to use Selenium to simulate the browser activity and store each researchers' name, institution, and their email to local. Since the email is given as images on the website, I used pytesseract to convert the image to text. 
* **Deployment:** This script helped to scrape 1200+ emails


### Professor Database & Email Automation
* **Context:** Scraping thousands of emails bring up the question of managing all the data. We also need to automate email sends to produce individualized email in mininum amount of time. 
* **Design:** I used MongoDB to store the name, school, email, whether the email is valid, and other information. Everytime I upload a .csv file, the program automatically checks for duplication, requests www.mail-verifier.com to check whether the email is valid, and stores the corresponding information in the database. I can then use www.mailgun.net to send valid emials and mark then as sent in the database. 
* **Deployment:** I created a database of 2200+ researchers in China, including IEEE, ICCV, IJCAI fellows and more. I sent 600+ emails and got ~15% responses. 
