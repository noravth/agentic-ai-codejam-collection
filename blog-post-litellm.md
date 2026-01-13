# Happy New Year and Happy Coding of AI Agents!

I hope everyone found their way into the new year and had some peaceful time over the holidays!

Being back this week, I started to try out all the cool announcements from last year. One of 
them is LiteLLM, where SAP contributed to function as an LLM provider. That means you can now
build AI Agents with LiteLLM and all the AI Agent frameworks that are compatible and provide
your Generative AI Hub credentials to connect to LLMs via SAP's AI Foundation.

I tried out CrewAI first because it is such a powerful and widely used framework and I have been 
curious and willing to try it out for some time now!

First things first: What is LiteLLM?
LiteLLM is a library that provides a unified, provider-agnostic API for calling large language models (LLMs) and handling common tasks (completion, chat, streaming, multimodal inputs).

It standardizes request/response handling, and includes utilities that speed up integration with agent frameworks and tooling.

That means you can use your Generative AI Hub credentials to build state
of the art AI Agents with any of the models available through GenAI Hub and any of the AI Agent frameworks compatible with LiteLLM. This combination is extremely powerful because that means you can use LLMs hosted or managed by SAP (Mistral, Llama, Nvidia) and models from our partners such as Azure OpenAI, Amazon Bedrock (including Anthropic) and Gemini.

-> check all the models here: https://me.sap.com/notes/3437766

And all the AI Agent frameworks including: CrewAI, LangGraph, PydanticAI, Doogle ADK, Strands SDK, OpenAi ADK, LlamaIndex, Microsoft Agents and many more. You can find a list with examples here: http://sap-contributions.github.io/litellm-agentic-examples/

Now to get started you need an SAP AI Core instance with the extended plan (on SAP BTP), that means you have access to Generative AI Hub and all the LLMs available. 
TODO Add picture of AI Core instance in BTP.
TODO -> Tutorial here: 

LiteLLM is directing calls to the LLMs through the orchestration service on Generative AI Hub. That means you do not need to deploy your models on SAP AI Core, you only need the out of the box deployment of the orchestration service. This way you can easily switch between all the models available via the orchestration service.
TODO: Picture of AI Launchpad showing models part of orchestration service deployment. 

On a side note: you do not need SAP AI Launchpad as the UI to do any of this. You can also deploy your models via API calls or the Python SDK here as shown here:.
TODO -> Tutorial on deployments here: 


You also need Python installed to install the LiteLLM library and in my case also CrewAI:

-> pip install litellm crewai

Ok now we can actually start with building our AI Agent with CrewAI. As the name suggests you build a crew of agents that have a set of tools available to accomplish certain tasks. CrewAI uses tasks to bridge the gap between high-level goals and concrete agent actions, assigning specific objectives and expected outputs.
