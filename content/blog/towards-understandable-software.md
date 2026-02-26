+++
title = "Towards Understandable Software"
subtitles = "Why programming sucks and how to fix it"
date = 2026-02-25
tags = ["computing"]
draft = true
+++

Programming sucks. Code sucks. It's hard to read, hard to test, and hard to maintain. Only a handful of people can understand any particular software project. These are major problems. I'm here to explain how we can fix them.

## LLMs aren't the Model

Large Language Models (LLMs) are becoming an important part of industry software development. Even experts with years of experience are using autonomous LLM agents to test, debug, and even write their code. They that they are capable of integrating with their environment, many of the logistical problems with LLMs have been mitigated.

Non-programmers have also turned to LLMs. Programming can be unapproachable. Many people have no clue where to start and, even if they did, no desire to learn the ins and outs of the syntax and libraries of a particular language. I regularly see people with little programming knowledge use LLMs to write them anything from simple personal scripts to tools to process scientific data.

I don't believe this is the result of LLMs being incredible programmers. Almost everyone in the field has seen the results of a session of vibecoding. Even if the tests pass, the resulting code is usually atrocious.

No, I believe programmers and non-programmers alike have turned to LLMs because programming *sucks*. There are so many conflicting software stacks, endless boilerplate, and annoying libraries. The work of the average software developer has been reduced to gluing libraries together rather than developing interesting code.

But the fact that programming sucks doesn't make LLMs suck any less. The major problems with them persist. They still are environmentally destructive, fundamentally based on stolen code, produce inconsistent code, and are bad for your brain. Overall, LLMs make programming worse than it has been before, despite their promise. We deserve better than current programming paradigms, but we also deserve better than LLMs.

## We Can do Better

We don't have to give up automation if we give up LLMs. We don't have to give up high levels of abstraction if we give up LLMs. We don't have to give up human-friendly interfaces if we give up LLMs.

The benefits promised by LLMs may not outweigh their costs, but we don't have to give up those benefits. We can have predictable, high-level, testable systems that make software more maintainable. We don't even have to give up using natural language to communicate with machines. We just have to take a different approach.

Instead of tackling the problem of writing code, we should tackle the software stack underlying the code. Instead of making it easier to write endless amounts of code, we should eliminate the need to write code at all. We should embrace the layers of abstraction that have led us to languages such as Python. When the urge to automate our layer of abstraction emerges, we should instead abstract it away.

The prevalence of LLMs has shown us that we need another layer of abstraction above the one we currently have. The urge to automate the process of writing code has shown us that we should abstract away the need to write code at all. We need a layer that allows thinking about software even closer to the ways humans think about software.

### Document the Yak

The first step on our journey of making software understandable is documentation. Programmers know that documentation is important, but for the most part we see it as something to tack onto the code afterward. We write the code, and then maybe add doc-comments to explain what outwardly facing functions do. If our users are lucky, we'll even write usage examples.

I propose we flip this. Instead of writing the code first and tacking on documentation, we write the documentation first and tack on the code. We tell humans what our program does and then we tell the computer what it does. This is a concept known as [Literate Programming](https://en.wikipedia.org/wiki/Literate_programming).

Imagine this: instead of reading other people's code and trying to parse their intentions form it, you read the documentation to understand their intentions and then you read the code. You no longer have to spend extra exertion trying to understand what someone else meant from what they've written for another audience (the machine). They've already explained it for you.

The best example I'm aware of that implements this is the [Entangled](https://entangled.github.io) bi-directional tangler. You can use it to write code embedded in documentation, but then also edit that code normally which it then propagates back into the code in the documentation. This allows programmers to use 

We could embrace this approach and document the entirety of our software stack, from the firmware that boots our computers to the Web applications we use to check social media. This would make every aspect of software more accessible to those who use and develop it.

This approach doesn't directly solve the ways that programming sucks, but it makes the sucky code we write more comprehensible. It solves provides an alternative for one use-case of LLMs: understanding other people's code.

### Abolish Code

But we can go further. Not only can we document our code—we can destroy it.

Code is a concept from a bygone era. We were forced to work with it because we used to interact with computers through terminals. We used keyboards to input instructions into a computer, which then ran interpreted and ran those instructions.

There's no reason we have to keep this approach. Insisting we communicate with our computers with barely more than a one-dimensional series of obscure symbols and keywords is a refusal to take advantage of how computing has changed over the last 40 years.

Embrace structure. Abolish code.

#### Embrace the GUI

I believe one important aspect to replacing code is embracing the Graphical User Interface (GUI). Most of us don't interact with our computers solely through text-based interfaces anymore. There's good reason for that! GUIs allow us to reason about concepts in more complex ways than a text-based interface. 

We can do the same for creating software. Integrated Development Environments (IDEs) can be more than just places to more conveniently edit code. They can become completely new ways of interacting with the development of programs themselves. This is already the case in some environments. We should go further.

Visual programming could become so ubiquitous and simple that anyone could create whatever they want without having to learn to code. I want to live in that future.

We don't even have to give up the code! The GUI version could merely be one of several human-editable representations of a program. Just as some people love text-based interfaces to their operating systems, some people will continue to enjoy code-based interfaces to software editing. It just doesn't have to be the default—or the only—option anymore.

One important thing to touch on is accessibility. While this kind of [visual programming](https://en.wikipedia.org/wiki/Visual_programming_language) is specifically designed to be more accessible, embracing visuals for software development has the potential to exclude people with vision impairment. I want to emphasize the importance of ensuring that, in one form or another, visual programming is always just as accessible to those who can't see it. This can take the form of strong screenreader integration, or even an alternative representation specifically designed to be just as richly understood audibly or tacitly.

#### Code is Cheap. Show me the Talk.

I've observed several people talking about how LLMs move the level of abstraction up one more level. They talk about how LLMs are what allows humans to interact with computers using natural language, and that we are approaching an age where human-written code will be a niche activity like writing assembly is now.

I don't believe this is the case. In my opinion, LLMs do not represent a layer of abstraction, but rather a layer of automation. It doesn't abstract away the code layer, it automates it.

In say this because layers of abstraction are meant to be predictable and reliable. The intentions at a higher level of abstraction are supposed to be represented accurately at lower levels of abstraction consistently. This is not the case with LLMs. Instead, LLMs stochastically interpret their prompts and guess intentions. They behave unpredictably. They automate the process of randomly approximating the output of a task. If LLMs are a layer of abstraction, they're an incredibly lossy one.

Still, [Torvald's quote](https://lkml.org/lkml/2000/8/25/132) can still be inverted. Instead of thinking about code, we can think about "talk". Because what if "talk" and "code" weren't different at all?

Humans evolved our own languages over the last several million years. Our individual languages represent rich histories and are well-adapted for expression between humans. While optimized for interpersonal communication, they're not optimized for predictable communication with machines. That's why we've used code for this purpose to this point. However, recent advances of Natural Language Processing (NLP) may be just what we need to create predictable pipelines from natural language to machine code.

This approach may not be able to express the same logical relationships as clearly as visual programming, but it's an approach that may be even more accessible to non-programmers.

Imagine being able to type instructions much like you might into an LLM prompt and create complete programs, but ones that are predictable and robust every time. Ones that build directly on other people's work through definitions.

This could even allow us to merge documentation and code even further. Taking literate programming and replacing the code with natural language until only documentation remains. The same writing we use to talk to other humans about how the program works could be the same writing we use to communicate with the machine.

This is meant to be deterministic. NLP can be used to parse semantics from the grammar wtihout the generative capacity of transformer models. That parsed grammar can be translated directly into an intermediate that is compiled according to platform requirements, just like any other programming language.

This deterministic quality means that your prompts can become your code reliably. This makes it fundamentally different than any LLM. It's a true layer of abstraction.

## We've Done This Before

None of these ideas are new. There have been previous attempts to implement these very ideas. A prime example of this is [Eve](https://witheve.com), a programming language and IDE meant to make programming more accessible to humans.

To do this, Eve takes a literate programming approach. They embed their domain specific data-oriented programming language in documentation that describes how the software behaves to other humans. The code is subservient to the documentation.

They experimented with going even further with this idea, trying to [replace their custom language with NLP querying](https://incidentalcomplexity.com/2016/06/14/nlqp/). Unfortunately, processing natural language comes with complexities they were not compared to handle. They did not have the resources to turn it into a reality. In 2016 more advanced forms of NLP weren't as accessible to companies that weren't focused on Machine Learning. [They even experimented with a GUI-oriented approach!]( https://incidentalcomplexity.com/2017/10/04/September/)

[A former Eve contributor also talks about some of the complexities of the project](https://mech-lang.org/post/2025-01-09-programming-chatgpt/). Their post also expresses some of the same concerns about the limitations of LLMs I do here. 

Unfortunately, the project was ended largely because it was [an ambitious VC-funded project that failed to monetize their product](https://news.ycombinator.com/item?id=45559031), so we never had the opportunity to see their ideas come to fruition. Could it be replicated and expanded with a better financial model?

It's possible natural language is fundamentally a leaky abstraction. But I believe it's worth another shot. The potential unlocked by giving the average person direct control over their computers deserves much greater attention. It deserves more attention than we're giving it. It deserves better than LLMs.

## Bringing it Together

Programming sucks. But that doesn't mean we should automate it away and have LLMs write everything for us. Instead, we should abstract code away, building on top of it to provide robust and deterministic systems that allow us to describe software at a higher level.

We should embrace visual, literate, and natural language programming in order to better communicate our intentions with machines and with each other. 

## Next Steps

I believe in the importance of making understandable software. To this end, I'm working on projects that further this goal.

Primarily, I develop [ReTangled](https://codeberg.org/liberty/retangled), an Entangled-compatable bi-directional tangler written in Rust. It's meant to extend literate programming as far as it can go while integrating it as tightly into existing toolchains as reasonable. As of writing, it's in the early stages of development. I welcome contributions!

Further than that, though, I want to explore more of the problem space I describe here. Specifically, I want to pick up in Eve's footsteps, maybe taking a slightly different branch. I want to create a highly-documented and accessible visual programming environment that anyone from new to expert programmers can find useful. That's still far out but that vision is my goal.

So please, join me! Let's start by better documenting our software and end with upending the very concept of programming.
