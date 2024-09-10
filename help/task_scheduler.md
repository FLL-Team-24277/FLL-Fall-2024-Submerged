Kids don't regularly pull updated code from github. We tell the kids to do a push at the end of each practice, and we have VS Code set up to do a pull each time they open the program, but sometimes they don't shutdown the program... they just close the laptop. So I like to add a task scheduler to do a pull every day at noon. That way I know they all have the latest code on their laptops at the beginning of practice.

Before you get started, copy the path to the local repository saved on the computer. For example

C:\Github-Projects\Fall-2024-Submerged

You will need that path during the task setup.

Click on the Windows Start menu and type "Task" and click on "Task Scheduler" (not "Task Manager"). Then on the right side, click on "Create Basic Task".

![01TaskScheduler](https://github.com/FLL-Team-24277/FLL-Fall-2024-Submerged/blob/main/help/images/01TaskScheduler.png)  

Give the task a name like "git pull" and put whatever you want in the description.

![02CreateBasicTaskWizard](https://github.com/FLL-Team-24277/FLL-Fall-2024-Submerged/blob/main/help/images/02CreateBasicTaskWizard.png)  

I choose to run the git pull at noon every day, so I know all laptops are updated by the time practice starts after school. You may choose a different time.

![03TaskTrigger](https://github.com/FLL-Team-24277/FLL-Fall-2024-Submerged/blob/main/help/images/03TaskTrigger.png)  

![04DailyRecurrence](https://github.com/FLL-Team-24277/FLL-Fall-2024-Submerged/blob/main/help/images/04DailyRecurrence.png)  

Chose "Run a program/script" for the action.

![05Action](https://github.com/FLL-Team-24277/FLL-Fall-2024-Submerged/blob/main/help/images/05Action.png)  

For the action, just type "git" and for the command line options, just type "pull"

Be sure to fill in the path that you copied earlier into the path field

![06StartAProgram](https://github.com/FLL-Team-24277/FLL-Fall-2024-Submerged/blob/main/help/images/06StartAProgram.png)  

That's it. All done.

![08Summary](https://github.com/FLL-Team-24277/FLL-Fall-2024-Submerged/blob/main/help/images/08Summary.png)  

You can try to run the task right now to see if it is working. On the right side, choose "Run". The window that pops up will only be there for a split second, so be sure to pay close attention. Maybe consider making some small change in the repository before testing so that there is something specific to pull. If there are no changes at all, the command goes very quickly.

![09TaskSchedulerFinished](https://github.com/FLL-Team-24277/FLL-Fall-2024-Submerged/blob/main/help/images/09TaskSchedulerFinished.png)  


