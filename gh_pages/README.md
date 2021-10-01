# How to host your website on GitHub pages 

## Static sites
Generating content dynamically can make a website slow. Therefore, a possible solition is using a static copy of the site. 

Installing WordPress on a local computer, creating the site and publishing only static content to the public web provides:

1.  free hosting for static websites with  [Github Pages](https://pages.github.com/)
2.  the speed and security of a static site
3.  the usability and resourcefulness of WordPress

### For this tutorial we will be using Windows, because we need to install multiple softwares which were developed for Windows/Mac. Therefore, if you are on Ubuntu I suggest to switch to Windows before continuing with the tutorial.


Follow step 1-3 on this website to create a github repository and set gh-pages as default branch:
https://www.hywel.me/static/site/wordpress/2016/07/17/fast-free-static-website-with-wordpress-and-github-pages.html

## 1. Create a Github Pages Repository to Host the Static WordPress Site
1.1. Login to your github account and under the repositories tab select new
1.2. Give your repo a name and select: "initialize with a Readme"

## 2. Create gh-pages branch and set as default branch
2.1. Click on the branch:master and type in a gh-pages to create a new branch
2.2. Go to settings -> branches
2.3. Set gh-pages as default branch
2.4. Select the 2 branches icon in the repo and delete the master branch

## 3. Clone GitHub repo to your local machine
3.1. Install GitHub Desktop app to easier manage github cloning, commiting: https://desktop.github.com/
3.2. Clone your github repo with the help of GitHub Desktop app 

## 4. Install a wamp server and Wordpress
To install a wamp server and Wordpress follow this tutorial:
https://zuziko.com/tutorials/how-to-install-wordpress-on-windows-using-wamp-server/

>*Note:* In case there is an error message after starting wamp, you need to  update the microsoft visual c++ package. Use the instructions in this video: https://www.youtube.com/watch?v=h8QDs2Ssr5s

## 5. Add the simply static plugin
Let's continue with the first tutorial, from step 4:
https://www.hywel.me/static/site/wordpress/2016/07/17/fast-free-static-website-with-wordpress-and-github-pages.html

5.1. Install simply static plugin
5.2. got to smply static plugin settings
5.3. set the destination url, which will be the url of your github pages repository. The static website URL hosted with Github Pages is shown on the Settings Page of your repository , it is the GitHub username followed by the repository name.
5.4. Set the local directory, where the static files will be generated. This should be your github repository folder.
5.5. Advanced tab: upload the wp-content folder,so that stylesheets and themes are processed to preserve the look of your site.
5.6. Save and generate static files


## 6. Commit changes and sync to Github
6.1. Commit the changes to Github
6.2. Check your repo for the files
6.3. Open the gh-pages url to see your website

## 7. Customize your website

7.1. Choose a new theme in wordpress
7.2. Customize it to your needs
7.3. Generate static files and replace the files in your local github folder
7.4. Commit the changes and enjoy your new website

## 8. Sources

8.1 Add the ASIMOVO logos from the drive https://drive.google.com/drive/u/0/folders/1P2MrBsEtDp4QgrDciogkGoJERmV7i3q8



 
