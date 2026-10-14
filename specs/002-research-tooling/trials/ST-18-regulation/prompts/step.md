4. **List what exists.** The state of the art of most aspects is written down.
   - Search for the aspect as wide as the owner stated it. Do not search for one use case,
     one industry or one product only.
   - Search for each candidate view in the words of that view. Do not search only for
     documents that you know by their title, or that carry the name of the aspect.
   - Search for the concerns of each stakeholder in the words of that stakeholder.
   - Find the existing descriptions first: standards, frameworks of foundations, the
     documentation of platform vendors, research, recognized books. Then find the practice
     sources.
   - Find the regulation, the governance and the public recommendations of the aspect also.
     Search for each of these kinds, in the words of each view and of each stakeholder:
     - laws and regulations that bind a group of projects or of organizations;
     - frameworks of governance and of audit, and the rules of an industry;
     - recommendations that a public authority publishes.
   - Give each one that you find to a reader. Do not leave one out because it binds only one
     industry or one region.
   - Find the maintained projects of the aspect also. Search for each of these kinds, in the
     words of each view:
     - projects that give the practices of the aspect as components that a project can use
       again;
     - tools that examine or measure how a project does the aspect.
     - open projects that many other projects depend on: what each one does for the aspect
       in its own work.
   - Give a file of such a project to a reader with the task `prompts/sample-reader.md`. The
     reader reports the tools, the integrations, the frameworks and the patterns that the
     project uses, and the principles that the project states.
   - Give also the writing of such a project about its own way of work to a reader with the
     same task: its documentation of the principles, its design notes, its rules for a
     contribution.
   - Save the report of a sample and put it into the index, as step 5 tells you for the
     report of a reader (`index.py take`). To get what the samples use, run
     `uv run factory/sota-research/scripts/index.py lines <work folder> --kind pattern`. The
     other kinds are `tool`, `integration`, `framework` and `principle`.
   - Put the pattern lines that describe the same pattern together into one named pattern,
     before you use them.
   - A principle of a project is the opinion of that project. Compare each principle with the
     standards and with the other projects. Where they disagree, write the disagreement into
     section 3.4 with the two sources.
   - Do not take a principle of one project as a checklist item for that reason alone.
   - Find the published statistics of the practice also: surveys and measurements that run
     for years and cover many projects. Record each one as a source.
   - Do not compute a statistic from your samples. The samples are few, and a thing that many
     projects do is not good for that reason.
   - A maintained project shows what is done and what can be used again. Record the date of
     its start and of its last release. Where it disagrees with a newer standard, write the
     disagreement into section 3.4.
   - Record each search query in `vetting.md`, in the list "Searches", with the view that it
     serves. The owner sees the list in the review.
