# algorithms
Miscellaneous algorithm implementations

## In The Future - 

## Steps to follow for contribution 

### 1. Fork the repo 

Get your own fork/copy of [algorithms](https://github.com/vidyabhandary/algorithms) by using the <kbd><b>Fork</b></kbd></a> button on github for the repository

### 2. Create a local clone of your fork

Clone (download) it to local machine using the command shown below. Replace with your GitHub username instead of YOUR-USERNAME.

```sh
$ git clone https://github.com/YOUR-USERNAME/algorithms.git
```

> This will create a local copy of the repository in your machine.

After you have cloned the `algorithms` repository in Github, move to that folder first using change directory command 

```sh
# This will change directory to a folder algorithms
$ cd algorithms
```

Rest of the commands are in this `algorithms` directory

### 3. Check configured remote repo for your local copy

You'll see the current configured remote repository for your fork with this command [*your local copy* has a reference to *your forked remote repository* in Github ] - 

```sh
$ git remote -v
origin  https://github.com/YOUR-USERNAME/algorithms.git (fetch)
origin  https://github.com/YOUR-USERNAME/algorithms.git (push)
```

### 4. Set up the upstream repo

Add a reference to the original [algorithms](https://github.com/vidyabhandary/algorithms.git) repository using the following command

```sh
$ git remote add upstream https://github.com/vidyabhandary/algorithms.git
```

> This adds a new remote named ***upstream***.

### 5. Check the remote and local repos
Use the following command to check all the remotes

```sh
$ git remote -v
origin    https://github.com/Your_Username/algorithms.git (fetch)
origin    https://github.com/Your_Username/algorithms.git (push)
upstream  https://github.com/vidyabhandary/algorithms.git (fetch)
upstream  https://github.com/vidyabhandary/algorithms.git (push)
```

### 6. Sync 

Always keep your local copy of repository updated with the original repository.
Before making any changes and/or in an appropriate interval, run the following commands *carefully* to update your local repository.

```sh
# Fetch all remote repositories and delete any deleted remote branches
$ git fetch --all --prune

# Switch to `master` branch
$ git checkout master

# Reset local `master` branch to match `upstream` repository's `master` branch
$ git reset --hard upstream/master

# Push changes to your forked `algorithms` repo
$ git push origin master
```
## To add a feature / algorithm

### 7. Create a new branch 

When you want to make a contribution, create a seperate branch using the following command and keep your `master` branch clean (i.e. synced with remote branch).

```sh
# It will create a new branch with name Branch_Name and switch to branch Folder_Name
$ git checkout -b Folder_Name
```

Create a seperate branch for contibution and try to use same name of branch as of folder.

To switch to desired branch

```sh
# To switch from one folder to other
$ git checkout Folder_Name
```

To add the changes to the branch. Use

```sh
# To add all files to branch Folder_Name
$ git add .
```

Type in a message relevant for the code reveiwer using

```sh
# This message get associated with all files you have changed
$ git commit -m 'relevant message'
```

Now, push your work to your remote repository using

```sh
# To push your work to your remote repository
$ git push -u origin Folder_Name
```

Finally, go to your repository in browser and click on `compare and pull requests`.
Add a title and description to your pull request that explains your effort.


