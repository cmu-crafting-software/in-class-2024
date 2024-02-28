# Lecture 13: Collaboration

Be sure you are paired up! (One group of 3 is ok!)

Go to: https://github.com/cmu-crafting-software/in-class-2024

## Create a new Kanban project board

1. Click `Projects-->New Project`
10. Use the default `Team Planning` template
11. Using the `+` button at the bottom, type `#`, select `in-class-2024`, and add a new issue to the kanban board
12. Drag the issue you created around to different parts of the kanban board
13. Click on the issue and notice that there is a project section in the issue that shows on which part of the Kanban board the issue presently resides
14. Notice that you can change the board location from within the issue as well. Try doing that now.

## Create an issue

1. Click `Issues`
1. Notice the issue you created on the Kanban board is also listed here
2. Click `New Issue`
1. Give the issue a title that includes your Andrew ID
2. Describe the issue
3. Assign yourself to the issue
4. Select the project you created and then choose a status (like `in progress`)
4. Choose some labels for the issue (like `bug` and `help wanted`)

## Make a change to your branch

1. Open a Codespace
4. Update your branch from main and push to GitHub
   ```
   $ git checkout <your andrewid>
   $ git status (to make sure you are on your branch)
   $ git fetch origin
   $ git merge origin/main
   $ git push
   ```
5. Make a change to your branch
   1. Make sure that the change to your branch is on GitHub (you may need to reload the page in your web browser)
   2. Copy `feb-28-collab/README.md` to a new file in your branch, `feb-28-collab/README-<andrew id>.md`
   3. Stage, commit, and push to GitHub

## Create a Pull Request

1. On the GitHub website, select your branch, click `Contribute` then `Open Pull Request`
1. Fill in the title and description of the PR
2. Assign the PR to yourself (on the right hand side of the screen)
3. Choose your group mate as the reviewer
4. Choose the project that you created
4. Choose some labels for the PR (you can create a new label, too, if you like)
6. Click `Create` 
5. Under Development, select the issue you created
7. Tell your group mate the PR#

## Review a Pull Request for someone else

1. On the PR that your group mate sent to you:
1. Click the `Files Changed` tab to see the changes
2. Select some lines by dragging the plus and add a comment
3. Click `Review Changes` and enter a positive comment
4. On the main PR screen, how has the `Review` pane changed?

## Merge your PR into Main

1. Go back to your own PR after your group mate has reviewed it
1. Read the review your group mate left
2. At this point you can either merge the PR as-is or push more commits to, e.g., address some issues that the reviewer had.
3. If everything looks ok, squash and merge the PR

## Post-merge status check

1. Do you now see your file on branch `main`?
5. Check the issue you previously created. What is its status now?
6. Where is the issue on the Kanban board? Is this the right location? Why is it here?



