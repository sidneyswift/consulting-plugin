# Social article source samples

These are source samples Sid provided as examples of the middle-length social article style. Study the structure, principles, and moves. Do not copy the phrasing unless explicitly asked.

## Tool calling interfaces

> mcps, apis, clis, are all ways to invoke tools, thats it
>
> the goal of this article is to help share how i think about tool calling, the different specifications, when to use each, and the underlying concepts
>
> as a thought experiment, consider what happens when you convert an MCP to a CLI, the actual underlying tools have not changed, all that's changed is your execution environment.
>
> hammering this point again, context bloat is not an MCP problem, it is a problem of the implementation of how tools are exposed to the model.
>
> if a company has an MCP server, you want it to have as many tools as possible as that's more capabilities your agent is able to do on your behalf
>
> my personal executor.sh instance has ~10,000 tools in it, a mix of MCP and APIs and agents are able to work beautifully with it.
>
> so, with it established that they're all the same underlying concept why do these 3 exist? when do you use one vs the other?
>
> MCP
>
> MCP seems to be the right protocol to use for any interactions that are with agents, some examples of this are:
>
> Claude Channels is built on MCP and allows you to push data back into a running session via an MCP
>
> MCP Apps allows for embedding ui directly inside of chats, i.e "show me a chart of my posthog data"
>
> MCP Elicitation enables getting actual input from humans, this is really useful when you need them to confirm something like "are you okay with analytics" or going to a url to perform an action
>
> MCP Triggers to notify clients of state changes
>
> now the trouble with these is there's a chicken and egg problem. most clients only implement support for MCP tools and that's it. what's cool though is you can actually work around partial client support but doing the same functionality over tool calls only as a fallback, which i'll have a longer post coming on
>
> APIs
>
> where i'm landing on APIs is they're great for raw data access and quickly converting your app to be agent accessible. APIs carry good information already about their descriptions, what operations are destructive / not destructive / etc
>
> to me, it doesn't make sense to try to get behavior like mcp apps, elicitation, triggers through OpenAPI as that's not meant to be for agents, mcp is
>
> CLI
>
> this is going to be controversial, but i really think that CLIs are just for humans when looking at the long term horizon. a bit part of this comes down to the known action space of a CLI, in that for people that want to know what an agent is actually able to do
>
> the other part about CLIs is requiring a unix shell to run them. when we look at enabling every person in the world to have a personal assistant or interact with their data through ai, the overhead of CLIs very quickly makes this not possible
>
> that's not to say that they're bad though, i would easily argue the CLIs produced by @steipete are state of the art for agents because of how much care has been put into the design of their interfaces, their ability to get data in hard to reach places, etc
>
> today CLIs provide the best debuggability, interfacing, data access, etc to agents because of the beautiful composability of bash and everything running them locally on your computer enables
>
> back in March we saw a lot of writing around 'Building CLIs for agents' and fundamentally it just comes down to bash being the wrong primitive for agents to be using. there's too many footguns for them to get trapped in i.e when they run a command that prompts for human input
>
> closing
>
> at the end of the day, you can convert an API into an MCP into a CLI back into an MCP back into an API
>
> they're all the same concept, giving the agent the ability to invoke tools, what changes is the amount of dependencies and capabilities the agent gets when using it
>
> APIs are probably fine for 90% of applications, CLIs are the best for agents today just due to the robustness of bash, MCP has a lot of potential to solve the problems presented by using CLIs today, however, it's going to require spec improvements and good harness implementations so hopefully fable comes back

## Hermes Agent for Product Managers

> Hermes Agent for Product Managers
>
> What is Hermes, and how is it different from Claude Code?
>
> Hermes Agent is an open-source agent runtime from Nous Research. It can run on your machine or on a remote server. It can use tools, load skills, keep memory across sessions, run scheduled work, spawn subagents, and talk to you through a CLI, desktop app, Telegram, Discord, or dashboard.
>
> Claude Code is best for a focused work session. You point it at a repo and ask it to inspect files, change code, run checks, explain the diff, and stop. The center of gravity is the codebase and the current session.
>
> Hermes aims at longer-lived agent work. Its center of gravity is the agent environment: memory, sessions, skills, gateways, scheduled jobs, and surfaces you can reach later.
>
> The practical split:
>
> Use Claude Code when the task is a bounded coding session.
>
> Consider Hermes when the task needs memory, repeat work, messaging access, or long-lived state.
>
> So the choice depends on the job.
>
> How is Hermes different from OpenClaw?
>
> Akshay Pachaar's Hermes masterclass frames the difference this way:
>
> Hermes packages a gateway around a learning agent. OpenClaw packages an agent around a messaging gateway.
>
> Both tools live in the same broad category: persistent agents, messaging surfaces, skills, tools, memory, and remote use. The difference is what each system seems to treat as the center.
>
> OpenClaw is more messaging-gateway-first. It is strong when you want an agent reachable through chat-like channels and workflows around that gateway.
>
> Hermes is more learning-agent-first. Its pitch is that the agent gets better from use. It keeps bounded memory, searches past sessions, writes or updates skills, runs background review passes, and can use scheduled jobs or subagents inside the same environment.
>
> The masterclass describes Hermes as combining three things that usually sit apart:
>
> runtime skill learning
>
> persistent multi-layer memory
>
> optional offline skill improvement through GEPA
>
> For a PM, the practical reading is simple:
>
> If the main job is "I want to message an agent from different places," OpenClaw is the adjacent reference point. If the main job is "I want an agent that remembers, builds skills from repeated work, and can run as a broader personal agent environment," Hermes is the system to study.
>
> Three real use cases people have said Hermes is good at
>
> 1. Source collection and research workflows
>
> The strongest PM-relevant example is Artem Zhutov's Hermes plus Obsidian workflow.
>
> He describes using Hermes from Discord to scan his YouTube home feed, pick the top videos, and add them to NotebookLM. The value is not that Hermes writes a perfect essay. The value is that it starts the research pipeline while he is on his phone. Fresh sources are waiting when he sits down later.
>
> For a PM, that maps to:
>
> collecting customer videos, docs, articles, or links
>
> pushing them into a notebook or research folder
>
> preparing the source set before synthesis starts
>
> This is useful precisely because it is small. Hermes moves source collection into the background before the PM sits down to think.
>
> 1. Memory and workflow capture
>
> The same Artem piece says Hermes wrote seven entries into his USER.md and created skills from completed workflows.
>
> One example: he finished a workflow around finding YouTube videos for NotebookLM, and Hermes captured the pattern as a skill.
>
> That matters because Hermes saved the workflow as a reusable instruction after the work happened. A normal chat tool would not do that unless the user manually wrote the process down.
>
> For PMs, this is useful in workflows like:
>
> weekly research prep
>
> meeting prep
>
> customer feedback triage
>
> stakeholder brief creation
>
> recurring market scan
>
> The caveat is obvious: memory can save the wrong thing. A system that remembers needs review, caps, and deletion paths.
>
> 1. Automated triage and briefings
>
> The Hermes tutorials repeatedly show cron jobs and "wake agent" workflows.
>
> One example is bug triage. A cheap script watches logs or new reports. The expensive model wakes only when something needs judgment. The agent verifies the report and sends a proposed triage summary or fix plan through Telegram or Discord.
>
> Another example: scheduled briefings. Hermes can run isolated sessions on a schedule and send the result to a messaging channel.
>
> For PMs, the most plausible versions are:
>
> daily competitor brief
>
> weekly customer pain digest
>
> new bug report summary
>
> stakeholder prep packet before a recurring meeting
>
> project status scan from known sources
>
> This is where Hermes starts to feel different from a normal chat UI. It can run away from the keyboard, then deliver something back into a channel.
>
> What kinds of PMs benefit from Hermes?
>
> Startup PMs and founder-PMs
>
> Startup PMs benefit if they already act like a product person, researcher, analyst, and operator in one body.
>
> Hermes helps most when a team has repeated, semi-structured jobs that nobody owns cleanly:
>
> tracking competitor changes
>
> collecting user complaints
>
> watching a bug or report queue
>
> preparing a founder for customer calls
>
> turning messy notes into a research packet
>
> The risk is setup drag. If a founder-PM spends three days tuning Hermes before proving one useful repeat workflow, the tool has already won the wrong game.
>
> Consultants and fractional PMs
>
> Consultants may be the clearest fit.
>
> They switch contexts often. They need client memory. They need to remember prior calls, source material, preferences, open questions, and promised follow-ups.
>
> Hermes' profile and memory model is relevant here because you can imagine one agent profile per client or workstream.
>
> The useful consultant workflow is not "write me a strategy." It is:
>
> gather the client source set
>
> maintain memory of what changed
>
> prep for the next meeting
>
> draft a follow-up brief
>
> keep client context from bleeding into another client
>
> That is a strong use case if the consultant has enough technical comfort to set it up or enough value at stake to justify help.
>
> Curious PMs
>
> Curious PMs benefit even if they never use Hermes day to day.
>
> Hermes teaches the shape of modern agent systems:
>
> the model is only one part
>
> tools decide what the agent can touch
>
> skills decide how it works
>
> memory decides what carries forward
>
> sessions decide what can be searched later
>
> the gateway decides where the agent can be reached
>
> That mental model is useful because agent products are moving from "chat with a model" to "design the work environment around the model."
>
> If you are curious, the right first move is not a Railway deploy. The right first move is to decide what job you want a long-lived agent to do. Then test the lightest version of that job.
>
> How Hermes works
>
> Hermes has a core agent loop.
>
> The model receives the prompt and decides what to do. It does not run tools directly. It emits a structured request. The Hermes runtime executes the tool, captures the result, and feeds the observation back into context. Then the model decides the next step.
>
> That loop matters because it keeps the model and the tool runtime separate. If a tool fails, Hermes can return the failure to the model as context. The model can then try a different next step.
>
> Hermes also separates tools from skills.
>
> Tools are executable powers:
>
> read a file
>
> run a command
>
> search the web
>
> use a browser
>
> call an API
>
> connect to an MCP server
>
> Skills are text playbooks. They are Markdown files that tell Hermes how to approach a repeat task. The source material describes progressive disclosure: Hermes can keep skill names and descriptions visible, then load the full skill only when it needs it. That keeps the context window from filling with every possible instruction.
>
> The memory layer has a few parts.
>
> First, Hermes uses two small files:
>
> MEMORY.md for agent notes, project facts, tool quirks, and things learned
>
> USER.md for user preferences, profile, and working style
>
> Hermes caps those files. That is not a minor implementation detail. The cap forces the agent to summarize and choose what matters.
>
> Second, Hermes stores past sessions in SQLite with full-text search. Old chats do not need to live in the active prompt. The agent can search for them when needed.
>
> Third, Hermes can use external memory providers such as Honcho or OpenViking. The Hermes memory-provider docs say Hermes allows one external provider at a time to avoid tool schema bloat. That is a useful design choice: more memory machinery can make the model worse if it buries the agent in choices.
>
> Hermes also has a gateway.
>
> The gateway lets the same core agent talk through different surfaces: CLI, Telegram, Discord, and other channels. This is why Hermes can feel more like a reachable agent than a local tool. You can message it later, and a proper host lets it respond without your laptop being open.
>
> Hermes also runs scheduled work.
>
> Hermes can run jobs through cron-like scheduling. More recent Automation Blueprints turn that into guided setup: the user answers questions instead of writing cron syntax. This is the kind of product detail PMs should notice. It moves the interface closer to the job the user wants done.
>
> Once an agent has tools, memory, and background work, it can do useful things while you are not watching. It can also save bad memory, run the wrong tool, burn budget, or act on a prompt injection. The more agent-like the system becomes, the more the boring parts matter: permissions, caps, review, logs, and rollback.
>
> Where PM OS fits
>
> The Hermes lesson for PMs is not that every PM should run a personal agent server.
>
> The lesson is that useful AI work needs a working system around the model.
>
> For Hermes, that system is the runtime: tools, skills, memory files, session search, gateways, scheduled jobs, and profiles.
>
> For product work, the system looks different:
>
> The system needs company context.
>
> The system needs product goals.
>
> The system needs team constraints.
>
> The system needs stakeholder context.
>
> The system needs reusable PM workflows.
>
> The system needs project memory.
>
> The system needs decision logs.
>
> The system needs review steps before context becomes truth.
>
> That is what PM OS packages.
>
> It is not a Hermes replacement. Hermes is a general agent environment. PM OS is a PM-specific working system that runs inside the tools PMs already use, mainly Cursor and Claude Code.
>
> The reason this matters is simple: most PMs do not want to assemble memory files, workflows, skills, and retrieval rules from scratch. They want the AI to understand the product, the company, the decision history, and the kind of PM work they are asking it to do.
>
> Hermes shows the shape of the deeper system. PM OS gives PMs a prebuilt version of that shape for product work.
>
> If you want the PM-specific version of this system without setting up Hermes first, PM OS gives you that starting point.
>
> Install AI PM OS today
