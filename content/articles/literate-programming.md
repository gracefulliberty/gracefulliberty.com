+++
title = "Document The Yak"
subtitle = "Why literate programming is vital"
date = 2026-02-28
draft = true
[taxonomies]
tags = ["computing"]
+++

Previously, I talked about the importance of making the process of software development [easier to understand](/blog/towards-understandable-software) for other humans. I want to delve into what I see as a vital component of this: literate programming.

Simply put, literate programming is what happens when you swap the normal places of code and comments. Instead of describing the code you write after the fact, you describe certain functionality and then write the code to express that functionality. This prioritizes explaining programs to other humans rather than to the computer.

<!-- more -->

While this approach does not replace code, it makes it incidental to the concepts being expressed. When you are forced to justify every decision to another human, another person can then reimplement it in any other language they please.

## Layers of Documentation

Over the decades, programmers have implemented some parts of literate programming into their stacks. We now have rustdoc, Chicken doc, and many other tools that let us document APIs to users. 

The best documentation is like an onion, an consists of several layers.

- End-user usage documentation
  - User guides
- Internals documentation
  - Contributing and maintenance guides
  - Architecture manual
  - API documentation
  - Documentation of functions
  - Documentation of code within functions

