---
description: >-
  Our AI Assistant can generate answers to your questions without you having to
  leave Slack
---

# AI Slackbot

This feature allows the AI Assistant to give answers to questions within Slack, and then post these questions/answers in the Questions section in your workspace!

**For data teams, this means:**

* No more answering the same question twice
* Protection against context switching
* Reclaiming time to focus on higher impact initiatives

**For data consumers, this means:**

* Get immediate answers to questions
* Self-serve data discovery
* Self-serve query generation

## How to use

1. Once you've connected your Slack workspace to Secoda by following these steps [#steps-for-setting-up-slack](./#steps-for-setting-up-slack "mention"), and you've enabled Secoda AI Assistant [#set-up](../../../features/ai-assistant/#set-up "mention"), you are able to utilize the Slack:AI Assistant feature.
2. Ask your question in the designated Data Requests Slack channel that is connected to your workspace
   * No need to prompt with a `/` command!
   * See [below](slack-ai-assistant.md#asking-questions-for-personal-use) if you'd rather not post these to the channel
3. If Secoda AI has the answer, it will return that answer directly in the Slack thread
   * Your teammates are also able to hop in this thread and provide their insights
4. The answer will show two options, :white\_check\_mark:**Answered** or :x:**Incorrect**, to which any user can decide if the response was accurate
5. If marked :white\_check\_mark:**Answered**, the question and the response will then be pushed into Secoda's Question section for all users to see and reference
6. If marked :x:**Incorrect**, the question will be pushed to Secoda without a response and the Admins of the workspace will be notified to provide an answer
7. Check out our best practices documentation on how to best implement this in your organization: [slack-less-than-greater-than-questions-workflow.md](../../../best-practices/slack-less-than-greater-than-questions-workflow.md "mention")

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/Slack%20AI_2%20(2).gif" alt=""></figure>

**Note**: Further ability to edit and add context to Questions pushed to Secoda can be found in the [ask-questions-in-secoda](../../../features/ask-questions-in-secoda/ "mention") section.

## Asking questions for personal use

If you have a one off question that you don't want to be posted in Secoda Questions, you can ask the AI Assistant questions in any DM or channel by prompting it by typing `/secoda-ai` followed by the question.

The AI Assistant will reply in the channel, but this response will be _Only visible to you_.

**Note:** As you can see below, it may take around 10 seconds to load a response:relaxed:

<figure><img src="https://secoda-public-media-assets.s3.amazonaws.com/Kapture%202023-06-12%20at%2017.29.32%20(1).gif" alt=""></figure>
