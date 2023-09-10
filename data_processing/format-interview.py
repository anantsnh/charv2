import json
import os
import re

output_directory = os.path.join("..", "data", "formatted_interviews")

# PASTE INTERVIEW BELOW THEN RUN SCRIPT
INTERVIEW = """
EZRA KLEIN: So let’s start where we are now. What can A.I. do now?

SAM ALTMAN: So I think we have just begun the realm of A.I. being able to be what we call general purpose A.I. instead of these narrow models that can do one thing. So now we have models that can understand to some sense, to some definition of that word, the world, what’s going on, and then a single model can accomplish a wide variety of tasks for someone and can learn new things pretty quickly. So last year, OpenAI released something called GPT-3. It’s a large text model. And that one model is now being used by thousands of people — developers more than that in terms of end users — for all sorts of tasks. And I think we will see, in the coming years, A.I. medical advisors that give anyone really high quality medical advice, higher than they can maybe get anywhere in the world, A.I. tutors that can teach you math or other topics. We’re starting to see people develop A.I. programming assistance that can help you write code. And these same models are being adapted for all of these different uses. And I think we’re starting now heading into a world where a lot of the things that people want, they can, through a text interface or a visual interface, have an A.I. help them do.

EZRA KLEIN: As I understand what these systems are doing now, they’re predictive. How is that intelligence?

SAM ALTMAN: So let’s think about what you need to make a smart agent. You need to understand what’s going on in the world, and you need to be able to think of new things, and you need to be able to take action to accomplish goals. In a very deep sense, I think the biggest miracle that we need to create the super powerful A.I. is already behind us. It’s already in the rearview mirror. We just — we need an algorithm that could learn and a network architecture that could somehow encode the knowledge and the capability to reason. And then once we have that, however imperfect it is, if you apply it to bigger and bigger systems with more and more computing resources, there’s no obvious upper limit. Once you have a system that can take in observations about the world, learn to make sense of them — and one way to do that is to predict what’s going to happen next — I think that is very near intelligence. So we have the ability to build systems that can learn, update, remember, create. We have the ability to build agents that try to accomplish a goal with that knowledge. And we’ve gotten surprisingly far just putting those few simple ideas together.

EZRA KLEIN: And so if I basically understand how GPT-3 works, it’s a system that has read a lot of stuff on the internet.

SAM ALTMAN: Yes.

EZRA KLEIN: And it’s predicting the next word in the sequence.

SAM ALTMAN: Slightly oversimplified but very close. Yes, it is trying to predict what comes next in a sequence.

EZRA KLEIN: And so to what you’re saying then, we have figured out algorithms that can learn.

SAM ALTMAN: Yep.

EZRA KLEIN: And then as they learn and as they know more, then as we are able to ask them to orient their predictions in different directions — that’s basically —

SAM ALTMAN: Yeah.

EZRA KLEIN: — a generalized intelligence that we could —

SAM ALTMAN: And there’s —

EZRA KLEIN: — that we could use.

SAM ALTMAN: There’s no obvious upper bound to that process. Think about how a kid works. They observe the world. They start to learn. They clearly make some predictions. And you can see when something doesn’t go the way they think it’s going to go and then they update. And the next time they’re not surprised or maybe they even can come up with new ideas based off of that. And you can also teach them stuff. You can correct them. And this idea of giving human feedback to a neural network in the way that we’ve given to our children for a long time, where we say, no, that’s right, no, that’s wrong, and the model, the A.I., or the kid, or whatever, is updated each time that happens. But then, let’s say, the agent can make better predictions, and do better, and need to get corrected less and less on increasingly subtle issues. There is no upper bound how far that can go as you think about increasing the size and scale.

EZRA KLEIN: I, obviously, don’t know how to use GPT-3 the way you do or what’s coming after it. But it sometimes seems to me that the harder thing to see from the outside of where all these are going is how flexible they are or they will become in being able to understand the way I want them to make a prediction. So there’s a lot that is being predicted, but right now it’s a mimicry. Like do stuff that is like the other thing.

SAM ALTMAN: Have you tried our newest instruction following model by chance?

EZRA KLEIN: I’m not sure.

SAM ALTMAN: You should. I think we’ve released something like that just quite recently where you can say, here’s what I want you to do and it will do it.

EZRA KLEIN: What have you done with it? What can it do?

SAM ALTMAN: A lot of — it’s still very simple, but a lot of simple tasks. If you say, summarize this for me or translate this into French, no matter what language it’s coming in as, or even a small multi-step problem where you need it to manipulate natural language, you can just say what you want it to do. And you can even say — I mean, you could probably say, write this in the style of Ezra Klein, and it would probably just do it.

EZRA KLEIN: What is the way A.I. changes the economy or changes people’s lives without using the word A.I.? What is the force it exerts on economic activity?

SAM ALTMAN: It’s a great question, Ezra. There’s a lot of different ways to answer that. But this idea that things that humans used to have to do that maybe they didn’t want to do, that took a lot of time, that took a lot of effort, that weren’t done that well, automated systems that can do those better. So we saw this happen with translation, for example, where if you couldn’t afford a translator, which most people couldn’t, and you were going to wander around some foreign country — I remember what that was like before we had A.I. translation and I know what it’s like now where I just speak into my phone and it speaks out the other language. And I love that. That really changes my experience of traveling. We’re beginning to see that now with certain subsets of the medical field where A.I.-assisted doctors can do better than doctors on their own, or let’s say computer-assisted doctors. But this idea that you can have intelligence, smartness, creativity — whatever you want to call it — that a computer is doing to help you do the things you want and have the life you want at a marginal cost of zero or very close to it, that’s I think a transformative thing happening in the world.

EZRA KLEIN: So that last piece is a piece I want to focus on, that marginal cost of zero. So the idea is that as machine learning, as these computer systems become better, basically everyone will have at their disposal a staff, like a corporation unto themselves, where they will be able to hire systems to help them out —

SAM ALTMAN: Yes.

EZRA KLEIN: — for almost nothing.

SAM ALTMAN: Yes.

EZRA KLEIN: Of course, that means — you were framing this a couple of minutes ago in terms of jobs people maybe don’t want to do or don’t do that well. But that also means jobs people do want to do or did do reasonably well, but not as well, go away.

SAM ALTMAN: That’s been happening for a long time and I don’t think we do a service to anyone to pretend that technology does not eliminate some jobs. Some jobs it just makes much better. But the arc of this has been that every technological revolution eliminates one class, one sets of jobs, and we find new ones on the other side that are hard to imagine from where we sit today. So before we had the computer, it would have been hard to imagine the computer programmer would be such an important profession. But I think if you look back at the great technological revolutions, which have been the punctuations where there’s been a lot of shift at once, there’s always been this worry. We’ve always found other jobs on the other side. Now, it may be that this time it’s different, right? If we really do think about what it means to have intelligence in a computer, maybe it’s different. But I so deeply believe that human ingenuity and desire for ever sillier kinds of status is so unlimited that we will find a lot of new things to do. I also think what we are likely to find is that a lot of classes of jobs that people talk about A.I. taking away stay, but the role of the human is very different. And the human does what humans are really good at. The A.I. does the part that the human might like to do less and that the A.I. is really, really good at. And you see this synergistic effect — I hate that word, but I couldn’t think of something else — where humans continue to be programmers, or doctors, or whatever.

EZRA KLEIN: Journalists maybe.

SAM ALTMAN: Journalists. But they focus on a different part of the job.

EZRA KLEIN: Two places I want to go with that. One is I’m usually on the side of this argument that says I don’t think machine learning is going to bring a near-term job apocalypse. But I’ve become friendlier in the past couple of years to the idea that it will destroy a lot of jobs pretty quickly. And to me it gets to the thing you were saying about generalized systems. In a lot of past revolutions, the revolutions, the technological changes, they happened fairly slowly and particularly their dispersal through society is pretty slow. And then second, they are general over time but they’re not general all at once. Now, if you think of machine learning as part of — and particularly of what we’re talking about here — as part of a long swing of automation, it isn’t all at once. But as I understand the way you see the world, that you think this is going to happen in a much more punctuated period than, say, electricity.

SAM ALTMAN: A couple of years ago, if you talked about general purpose A.I. at all, people said that’s ridiculous, it’s not happening. If you talked about systems that could really do meta-learning and learn new concepts quickly that they weren’t trained for, people so that’s not going to happen. And we’ve gone from a world where many of the experts in the field said that was sci-fi and irresponsible to talk about to clear existential proof that we have it. And it certainly doesn’t seem to be slowing down. Moore’s law, in varying definitions — but let’s say that was like a doubling of transistors every two years — maybe A.I. is growing at a rate of 10X per year in terms of these model sizes and the associated capabilities. So I do think we’re on a very steep curve. We will hit limits, but we don’t know where those will be. We’ll also discover new things that are really powerful. We don’t know what those will be either. We’re deep in the scientific discovery phase, which is awesome. It’s so exciting and fun. But I think what we can say is that we are on an exponential curve. And when you’re on an exponential curve, you should generally, in my opinion, take the assumption that it’s going to keep going. And humans are very bad at intuition for this. Trying to think about exponential curves for stock prices, for technology, for population growth, whatever —

EZRA KLEIN: For viruses.

SAM ALTMAN: Viruses. Very difficult. I had this moment that I’m sure you had one, too, when it looked like COVID was really going to take off and most of the world wasn’t paying attention. And I was walking the streets of San Francisco one night at like 10:00 p.m. walking home and everybody was just like frolicking and doing their thing. And it was just like, this is the last moment of normalcy and no one’s paying attention, because most people don’t understand exponential curves. And it was such a strange feeling and I’ve often thought about the parallels of that moment that hit so viscerally with A.I.

EZRA KLEIN: My own version of that — I remember sending an email to my entire family and saying, you need to go to the grocery store. In three weeks, you’re going to be living in a different world and you need to listen to me on this. Let’s talk about where exponential growth gets us in. You’re saying there’s a 10X-ing every year. That’s pretty big.

SAM ALTMAN: Yeah.

EZRA KLEIN: 20 years from now, what are you confident A.I. will be able to do and what do you think it is likely that it will be able to do?

SAM ALTMAN: Man, 20 years was a hard time frame.

EZRA KLEIN: Let’s do 10.

SAM ALTMAN: Let’s do 10. 10 I can do. In 10 years, I think we will have basically chat bots that work for an expert in any domain you’d like. So you will be able to ask an expert doctor, an expert teacher, an expert lawyer whatever you need and have those systems go accomplish things for you. So you’re like, I need a contract that says this. I need a diagnosis for this problem. I need you to go book me this flight. I want a movie created. I want you to make me an animated short or a photo realistic short that looks like this. I need you to help me write this computer program. So let’s say most repetitive human work and some creative human work you will be able to ask an A.I. to do for you. And that is a massively transformative thing.

EZRA KLEIN: I want to get at whether we are talking about a singular when we talk about an A.I. system or a plural. So the natural metaphor in people’s mind will be a software program. I buy some stuff from Microsoft. I buy some stuff from Apple. I buy some stuff from all kinds of developers whose names I forgot. My understanding of the way the A.I. systems are developing is that it’s turned out using the big machine learning neural networks that have turned out to be successful. You need ungodly amounts of data and amounts of computer power. And that means only a couple groups are big enough to build these general intelligence systems, assuming they do get built. And so is the world you’re talking about here a world in which OpenAI and maybe a couple other players have a system that is licensed out and everybody is building on top of that? Is it all just coming from you? What is happening here economically?

SAM ALTMAN: I think it’s going to be somewhere in between these narrow models that anybody creates and these mega models that only a few people can create. There’s this concept of fine-tuning. So where someone like OpenAI creates this powerful base model that only a few organizations in the world can do, but then maybe want to use that for a chatbot, or a customer service agent, or a creative multiplayer video game. And you take that base model and then with just a little bit of extra training and data, you push it in one direction or the other. So I could easily imagine a world where a few people generate these base models and then there’s the medical version, the legal version, whatever else, that get fine-tuned or polished in one direction or another. And a lot of people — a lot more people are capable of doing that. We’re starting to experiment with offering that to our customers now. But I could see a world — and I think it does no one any good to pretend otherwise — where as these models get really smart, the general purpose one can just do everything really well. And this idea that we think right now — that OpenAI thinks — which is we’re going to push one to be a coding expert and one to be a medical expert, turns out not to be necessary because 10X compounding is just so powerful that 10 to the 10th 10 years from now — the base model is plenty good at everything.

EZRA KLEIN: Staying on the idea of the big base models, as I understand it, there are a little handful of companies who are in the race to build one of these in a serious way. You’re one of them. But DeepMind is another. There’s a lot of work happening in China. Players in America like Amazon and Apple are trying to create — maybe not always general but pretty big things. How should I feel about the idea these will be privately owned if they’re going to be this powerful?

SAM ALTMAN: Strange. If we think about the major big iron engineering projects of the past, like the ones where there were large geopolitical and certainly social consequences — just to pick two examples to talk about here, we could talk about the Apollo project and the Manhattan Project — you can find different cost estimates of what those were. And who knows what you want to believe, but let’s say something with the word $100 billion in it. Those really took the wealth of nations to do. No company like us was going to do that, right? But the cost of technology does its thing. Companies and people get wealthier over time. You now do have a world where certainly the mega caps like Google can join this effort. But even much smaller organizations like OpenAI can get enough capital together — barely — to be able to be competitive here with what anybody else can do. So that’s weird. I have misgivings about that. Probably the non-technical thing I think most about is — let’s say we do make the true AGI, like the one from the sci-fi movies.

EZRA KLEIN: The Artificial General Intelligence?

SAM ALTMAN: Yeah. How do we want to think about how decisions are made there, how it’s governed, who gets to use it, what for, how the wealth that it creates is shared? If this is going to be one of these species-defining moments, it for sure should not be in the hands of a company, certainly not ours. But saying what we want the structure to be there, how we want to make decisions about it, what the equivalent of our Constitution should be, that’s new ground for us and we’re trying to figure it out now.

EZRA KLEIN: OpenAI begins as a nonprofit.

SAM ALTMAN: Yeah.

EZRA KLEIN: It becomes a for-profit, in part, because it needs to raise money and resources. So it got a billion investment that’s partially money, partially compute power from Microsoft.

SAM ALTMAN: Actually it was all in cash, but we spent most of it on compute —

EZRA KLEIN: Oh, there you go.

SAM ALTMAN: Close enough.

EZRA KLEIN: But partially on Microsoft computing power, correct?

SAM ALTMAN: Yeah.

EZRA KLEIN: Yeah. One of the worries I have about this is that even if people want to be very cautious about what the incentives of it are, that just in order to do it, you have to submit to those incentives. That just in order to raise the money, there has to be a business model, a backer. And I was reading that and I wondered this from a different direction, too. Was that a missed opportunity for the public sector? Should it be that the public sector is spending the money to build this either by funding groups like yours or a consortium of academic groups or something?

SAM ALTMAN: A little known fact, we tried to get the public sector to fund us before we went to the capped profit model. There was no interest. But yeah, I think if the country were working a different way — I would say a better way — this would be a public sector project. But it’s not and here we are. And I think it’s important that there is an effort like ours doing this. That even if not an official American flag effort, we’ll represent some of the values that we all hold dear. That’s better than a lot of other ways I could imagine someone else doing this project with us going. And one of the incentives that we were very nervous about was the incentive for unlimited profit, where more is always better. And I think you can see ways that’s gone wrong with profit, or attention, or usage, or whatever, where if you have this well-meaning people in a room, but they’re trying to make a metric go up into the right, some weird stuff can happen. And I think with these very powerful general purpose A.I. systems, in particular, you do not want an incentive to maximize profit indefinitely. So by putting this voluntary cap on ourselves above which none of the employees or investors get any more money — which I think if you do have a powerful A.I., will be somewhat trivial to hit — I think we avoid the worst of the incentives or at least the one that we were most worried about.

EZRA KLEIN: How about speed? So there’s an incentive to get there first. There’s going to be huge financial returns and otherwise returns to being the first one. You’re to some degree in a race with other companies to do it. I’m not saying that leads to cutting corners, but it leads to things where maybe you’d ideally want to wait for a governance structure to emerge, want to wait for a public conversation to happen. Well, if you don’t do it, the other folks will. And one of the constant ways things get justified in both government and business is that better us than them.

SAM ALTMAN: For sure. So I think we were able to design a system that addressed a lot of the incentives that I was particularly concerned about. The one that remains that I am — for the entire field, not just us — most concerned about is actually closer to the super powerful systems like the ones that people talk about creating an existential risk to humanity where there’s a race condition. And that I think will be on us and the other players in the field to put together a sufficient coalition to stop ourselves from racing when safety is in the balance. And we’re trying to figure out how to do that. That’s part of the governance question. Before you push go on this extremely powerful system, you would like as much time as you can get — and it won’t be totally in your control, because some other government can be doing whatever. But you’d like as much time as you can have to be really thoughtful about do we understand what the system is going to do.

EZRA KLEIN: And how do you get that time?

SAM ALTMAN: You have people partner and say, OK, lots of other industries have done this. I think the recombinant DNA conversations in the ’70s are a good example. But you say, we’re the experts on this. We’re the set of companies with the resources to do this. How can we work together to make sure we all have the time we need?

EZRA KLEIN: Is there a different kind of pressure that comes from the geopolitical push? It was interesting to me you used the metaphor of an American flag operation. So there’s a competition between you and other American companies. And then there is the sense that there’s also a competition from China, potentially, certainly down the road other countries. That can create a different kind of pressure. It could even be a pressure coming from the public sector. But a pressure to finish first.

SAM ALTMAN: This is something that some parts of the field have spoken about for a long time, which is, sure, the private sector companies can do whatever they want. But what if there’s huge public sector pressure? And that I don’t think we’d be in a position to have too much of an impact on. You

EZRA KLEIN: Mentioned before the cap on profits, which I believe for you all is 100X.

SAM ALTMAN: It started as that. It’s come down every time we’ve raised more money. So it’s the —

EZRA KLEIN: Got it.

SAM ALTMAN: — single digits now.

EZRA KLEIN: So there’s a question of how much money people can make and there’s a question of how money gets made.

SAM ALTMAN: Yeah.

EZRA KLEIN: And I’ve been thinking a bit about that as an important incentive question. So I’ll use your competitors over at Google as an example here. I worry a bit that if the big A.I. system is built by Google, it’s going to be oriented towards being very, very, very good at manipulating consumer preferences. It’s an advertising-based business. Other great interesting internet companies ended up building themselves around manipulating how people spend money online. I wouldn’t like to see something this powerful done that way. But Microsoft has other ones. You guys have other ones. It got me thinking about whether or not there are ways to shape the direction these systems are tuned in in useful ways. Like for instance, you could imagine a prize system where the public sector puts out multibillion dollar prizes for solving this technological problem, this scientific problem.

SAM ALTMAN: Yeah.

EZRA KLEIN: Tell me a bit about this end-game business models here. What they are turning out to be and what the options for them are?

SAM ALTMAN: So I can’t speak to what Google is going to do other than I probably won’t like it. [LAUGHS] But I could tell you how we’re thinking about it and how I hope other people will, too. What we’re excited about doing is the best research in the world and trying to build this eventually quite powerful general purpose system. What I think we’re not the best in the world at, nor do we want to really divert our attention to, are all of the wonderful products that will be built on top of this. And so we think about our role as to figure out how to build the most capable A.I. systems in the world and then make them available to anybody who follows our rules to build all of these systems on top of them. We have thought about prizes. You can imagine saying whoever — here’s this API. Do something great for the climate and here’s an incentive to do it. Or any number of other categories. But I do trust that on the whole if we can deliver super powerful new tools at an affordable price, the market will do its thing and we will get wonderful solutions to some of the most pressing problems facing humanity.

EZRA KLEIN: So you don’t think pro-social goals need to be built in by something explicit? You think that — you think certainly once you can just ask questions, at least those questions will be asked and they’ll be answerable?

SAM ALTMAN: Yeah, I mean, I think we’re going to do it, too, because it seems like a good thing to do. But I do think that even without that incentive, a lot of great pro-social things will happen.

EZRA KLEIN: So you have a version of this. You say that the rallying cry for this generation should be a Moore’s law for everything.

SAM ALTMAN: Yeah.

EZRA KLEIN: Tell me about that idea.

SAM ALTMAN: Look, it’s not a popular moment to say something positive about capitalism, but I will anyway. Which is that I think the power of capitalism has done more to help more people than probably any other single idea in human history. And the innovations, the new technology that we have both developed and gotten into the hands of people and the almost unimaginable improvements to quality of life, even though it’s fun to talk about how awful the world is and it is in many ways. That’s great. And part of the reason that has happened is things have gotten much cheaper. Pick your example. The cost of an hour of light at night, the cost of computing power, the cost of — so many things are now free that when we were kids were not. Entertainment, high quality education. You can go learn anything you want on the internet so well. It’s amazing to me.

EZRA KLEIN: My family, when I grew up, a lot of it was in Brazil. And long distance calls were a big deal.

SAM ALTMAN: Yeah.

EZRA KLEIN: And now it’s like every morning my kid is on FaceTime with his grandparents.

SAM ALTMAN: Yeah. And this relentless march of technology making the things that we need and want cheaper and cheaper and cheaper, that’s great. That’s how people’s lives get better every year. And all of us want our lives — or almost all of us — want our lives to get better every year. I think one of the big promises of A.I. is because of this idea of the marginal cost of labor going towards zero, things can get dramatically cheaper quickly. And way more of us can afford way more of the things that we want. And for a generation that has had a lot of, I think, economic headwinds and a deck stacked against them, I think this is a specific thing we can imagine that gets a lot of people’s lives way better pretty quickly.

EZRA KLEIN: So I want to make this specific. When you talk about a Moore’s law for everything, things that are expensive, that millennials, zoomers are having trouble affording when it was sometimes easier — sometimes also not — for their parents.

SAM ALTMAN: For sure.

EZRA KLEIN: But housing is very, very big in this. Health care is big in this.

SAM ALTMAN: Higher education, I think if we look at those three.

EZRA KLEIN: Higher education is huge. Those three are big. And I would say housing is primarily a zoning problem. In health, technology and the cost of technology is a real player there. And then there’s a fair amount of regulatory questions in both of them. So how does building A.I. allow for a Moore’s law in health education and housing?

SAM ALTMAN: So I think technology is a necessary, but not sufficient, part of the solutions here. I think that if we can’t get the politics and the policy right, it will face a lot of headwinds. I can still imagine it working on its own in some cases. I think there’s a lot of people who are paying $75,000 a year for college right now sitting at home on Zoom realizing that they can watch better lectures than they are. And I think a lot of things in higher ed are going to change no matter what the policy is. But I think if A.I. and policy can work in harmony, or let’s even say technology and policy can work in harmony, we can get to a much better outcome much more quickly than we otherwise might. And I think — again, to stick on the example of higher ed — I have never seen more energy from the consumers, the people who are going to college or thinking about going to college soon, saying, what am I really doing here and maybe there’s some much better way. So that’s the kind of pressure where I think things can change super quickly. The prestige of a degree from a top college probably doesn’t go away that quickly, but maybe a lot of the rest of it does.

EZRA KLEIN: How about housing?

SAM ALTMAN: I think it is time to consider radically new ideas there. I mean, it’s just so sad to me to watch what San Francisco is doing to itself. I think it’s so incredibly unfair. It really bothers me that it’s people who would describe themselves as liberal and progressive that are most in the way of, I think, the justice that comes from affordable housing and access to opportunity with that in the places where it matters most. And I think we should continue to fight that as hard as we can. But we should also realize that maybe we’re dealing with people here who are not reasonable actors. And there may be other cities where it’s just much easier to solve this problem. I think there’s been a mini-boom in new real estate startups as people in the pandemic have thought about leaving the big cities, where people can realize, wow, I can build a new house in some other city for not that much money and I can get exactly what I want. And I can now do it quickly with technology, surprisingly affordably, and maybe a competitive market will do its thing here.

EZRA KLEIN: You’re giving me, though, the answer here that I give to people when I’m in a technoskeptic kind of mood, which is, well, the problem in our way on a lot of things is not that the technology isn’t there. It’s that the political will isn’t there. It’s that the structure isn’t there. It’s that there are other impediments. So you have this piece about how A.I. is going to move all this power from labor to capital and it can transform humanity way for the better or not. That’s where the Moore’s law for everything idea comes in. What is the role of the system you’re building here? How is it going to help housing or any of this?

SAM ALTMAN: I mean, technology has already done a lot to help housing, I would say. And one specific thing that it did was enable remote work. And so, fine, a city like San Francisco is not going to be reasonable on policy. People can live elsewhere and still work for the most important companies in the industry that have been here. And they are freed from some of the geographic constraint. Look, remote work certainly does not work for everything and it’s not something that I’m personally excited to do. But I think it does work for a lot of things and a lot of people. And I think that’s an example of where faced with a seemingly intractable political reality, technology produces a solution that is a total curveball and not that imaginable a few decades ago.

[MUSIC PLAYING]

EZRA KLEIN: Tell me about the underlying idea that A.I. will move not just money, but also power from labor to capital.

SAM ALTMAN: I think the best way to frame this is this idea that the marginal cost of an A.I. doing work is close to zero once you’ve created this model, which requires huge amounts of capital, and expertise, and difficulty, and data to do. And I think it’s a very interesting question about who should benefit from that if — who generates the data or whatever. But once you train this model — maybe you used to have to pay an expert lawyer $1,000 an hour to answer a question or a computer programmer $200 an hour. And there weren’t that many and they had a lot of — you needed it and that was the market. That was what it was worth. And that was what people were able to command. But maybe now it costs a couple of cents of electricity for the computer to think or less. And you can do it as many times as you want. You can get the answers that no human could come up with. Labor then — in this case, extremely high-skilled and highly paid labor — all of a sudden has a lot less power, because the services are avA.I.lable at a wildly different cost.

EZRA KLEIN: So you write in the piece and that three things follow from that. One is that phenomenal wealth can get generated, because goods and services can become so cheap and so widely deployed that very rapid social change follows that because you’re just undergoing an extraordinary upheaval in the economy. And so then you have this kind of branching possibility, which is either very high standards of living for everyone or not. Some people get better entertainment and whatever, but they never get back the dignity, they never get back the money they were making.

SAM ALTMAN: Yeah.

EZRA KLEIN: How do you assess the political economy of A.I.?

SAM ALTMAN: I’m curious if you agree with the first two — if you think the first two things are going to happen.

EZRA KLEIN: Phenomenal wealth and social upheaval?

SAM ALTMAN: Yeah.

EZRA KLEIN: If you’re right about what the systems can do, definitely that will create wealth, right? I mean, it just has to. I think it’s almost mechanical. Upheaval to me is about how quickly it happens. And I suspect it could be technologically possible far before it is actually happening, or that the dispersion of the technology might be a lot slower than the realization of it. So you mentioned a minute ago lawyers. You ask lawyers questions because you need answers. You also ask lawyers questions because if you don’t get the answers from them, you might get sued. And so the question of when do you not get sued for asking the question of your system, as opposed to of the lawyers, is to some degree a regulatory and judicial issue more than it is even a technological one.

SAM ALTMAN: Yeah, that’s why I assume there will be these hybrid models where an A.I. is helping the lawyer, but the human lawyer and the existing system of the protection that you get from that is still the one giving you the answer. So maybe what happens is you still go to a lawyer, but that lawyer can be a factor of 10 or 100 times more efficient and they don’t need the staff of researchers they have today.

EZRA KLEIN: So I could see that and I think that makes sense. But that’ll reduce the amount of economic upheaval it brings. Health is a really big one. I’ve done a lot of work on health care over the years. I find it very hard to think through what the effect will be here. But let me put it this way. I’ve got a long running argument that we think too much about price in health and not enough about value. So budget work in Washington is always dominated by these graphs that show like by 2070, 50% of the economy is on health care. And people will say that’s wild. We can’t have 50% of our GDP going to health care. But how wild it is depends on what that is buying you, what the value of it is.

SAM ALTMAN: For sure.

EZRA KLEIN: If we’re spending 40% of GDP on health care, but everybody is living a healthy life till 200, maybe it’s fine. If we’re getting what we’re getting now, it’s terrible. And so one of the questions I don’t really know how to answer is does A.I., whether or not it is being used with doctors and nurses or otherwise, does it actually change radically the development of drugs, the device orientation and devices we’re able to use? Do we get way better at spotting things on radiology, which I think is pretty likely. So how do you change the value? You might not see that show up in wealth statistics exactly, but it would be a huge improvement in utility and how humans live. And so that stuff is very interesting.

SAM ALTMAN: I think wealth is definitely an imperfect metric. And I think price is even more imperfect. I totally agree with you, by the way, if we had a magic pill that everybody could take and have an extra 20 years of perfect health span and that cost 40% of GDP or whatever, maybe it’s fine. So I think these metrics are all imperfect. And what we really want is someone’s overall quality of life, and happiness, and fulfillment, and contentment and whatever. But I think for something numeric that we can measure today, wealth is the best thing. And I do think in terms of the branching that you talked about, somehow or other — this is maybe the techno-optimist in me — almost everyone’s lives are going to get better. People will demand it. And the question is, what form is that going to go in? I don’t actually subscribe to the Silicon Valley UBI will solve all problems. We can just do that and stop talking about it. I think it’s actually a small part of the solution. But I think we’re going to do it. I think somehow or other that’s going to happen. But for me then the question is, how are we going to construct the rest of society in a way that people have the dignity, the ability to decide where we all collectively go that is so important?

EZRA KLEIN: Well, let’s talk about UBI for a minute, because the place you go with this in your piece is toward something you call the American Equity Fund. I think actually a useful way to think about it is universal distribution of wealth.

SAM ALTMAN: Yeah.

EZRA KLEIN: Talk through that idea.

SAM ALTMAN: A thing that I did not understand when I was a kid is the difference between salary and equity ownership. And I assumed that the way people got rich was salary. And I knew that people traded stocks, but I didn’t think it was a big thing and not that important and it was basically about you get paid monthly. And really I think the way that value gets created is the compounding effects of equity, basically. So that’s the pro case on capitalism is that that works really well. The negative case is most people don’t own very much equity or land. I said in the piece that I think land and shares of companies are going to be the two dominant sources of wealth in the future. And so better than a government paying you some fixed fee every month is where citizens of a country own a slice of the important asset classes of the future. And that that’s how wealth gets redistributed, which I think is different than redistributing the equivalent of salary. Much more important.

EZRA KLEIN: I probably would agree with that. The problem I see — and this is why I asked very specifically about the political economy of A.I. So in this piece, you make an argument about how it’ll change the distribution of money and how could you tax around that. But this is one of those places where power really matters. And so another way of saying what you’re saying is that A.I. will make owners of capital and land much more powerful. And we are then somehow going to tax the owners of capital and land much more aggressively. And one of my, certainly, concerns about the world being sketched here is that my sense as a political person is you would somehow need to get a more equitable distribution of power in order to have the more equitable distribution of resources.

SAM ALTMAN: Totally agree with the statement about the equitable distribution of power being the important thing. Unlike paying cash transfers, I think if you’re actually transferring shares in these companies and the accumulating wealth there, or the ownership of land, or whatever else, that actually transfers some of the power over time, too.

EZRA KLEIN: But in order to get to that policy, you need the power to transfer first.

SAM ALTMAN: Yeah, here’s where we’re deeply out of my area of expertise. So I will ask you, what do you think it takes to get something like this in place?

EZRA KLEIN: I don’t know. I’m not sure you can. We were talking about this before we started the show, but something I’ve been starting to try to think through is how do you have a technologically aware progressivism. Have you ever read the book, “Fully Automated Luxury Communism”?

SAM ALTMAN: I’ve heard the phrase.

EZRA KLEIN: The argument it makes is that the set of technological changes coming down the pike — of which A.I. is central to that, but it’s not the only one — they actually make a case for much more radical form of public ownership. He’s using communism a little bit facetiously. But forms of communism, of socialism make a lot — of planning, of ownership, make a lot more sense under the technological structure that’s coming. But the question then becomes in order to have that happen, I think you actually need to set up the politics before the technology hits. Because if the technology hits first and then it just pools power among the people who own it, well, power increases its own wealth and increases its own power. And then we got these crazy A.I.s that are out there trying to manipulate public opinion and whatever else. It can get a little bit dystopic. And it’s not all going to happen overnight, but I do think this is a real — it’s a real question for me and it’s one reason I’ve become — in some ways what I want to see is a politics on the left, or on the progressive side, that is simultaneously more pro technology but is trying to take a stronger hand in predicting and then guiding that technology. But that’s really hard. I mean, we can’t pass even simple things right now. So the question of how we do it — I mean, I don’t know how we do basic climate change legislation. So how we completely restructure the way taxation works in this country when one of the two major political parties has literally signed a pledge to never raise taxes for any reason on anyone at any time? I don’t really think it’s a question that is answerable. But I am worried about what happens if some of these things hit and we haven’t come anywhere near an answer.

SAM ALTMAN: Our version of this is that technology is good, capitalism is fine, but you can put structures in place now that get you to the goal that you want. And I think we have this thing where hopefully we design a structure that let us benefit from capitalism to bring the thing into existence and I think that we couldn’t do without it. But once we’ve hit certain return thresholds, we have already figured out how our public ownership is going to work.

The ink is dry on that. And I think that’s cool. And I think more people should be doing things like that. And I think there may be versions of that that we could get done as a policy conversation, where you say this is how it’s going to work now. Don’t freak out too much. But here’s where it’s going to transition to over time.

EZRA KLEIN: One of the problems, though, with the policy conversation is that this is the set of issues it’s way behind on. So there are topics we know how to talk about in Washington from a policy perspective. Taxes is one of them. But I mean, you were saying earlier in the show that at least the power of these systems is on an exponential curve.

SAM ALTMAN: Yeah, taxing income — fighting over the rate on income tax is so the wrong way to be thinking about this.

EZRA KLEIN: And my concern is that to the extent there is a Washington conversation over — artificial intelligence is one of the set of technologies I’m interested in and worried about. But to the extent there’s a Washington conversation about it — and you probably know this better than I do — my sense is it has three prongs. It’s about algorithmic bias, which is important.

SAM ALTMAN: Yep.

EZRA KLEIN: It’s about competition with China.

SAM ALTMAN: Yep.

EZRA KLEIN: And it is on the margins about how do you subsidize maybe academic access to enough computing power.

SAM ALTMAN: The first two seem to dominate.

EZRA KLEIN: But yeah — so I mean, it’s basically it’s bias, it’s national defense, and then it’s some other stuff, like a grab bag. It’s not really about what do you do if society begins changing really fast. And also — and I mean this as exactly as important — what do we want from it as a public and how do we get that from it?

SAM ALTMAN: Let me tell you something. If you walk into one of these rooms and you — you know, they’re like, oh, I want to learn from you. What should we be thinking about A.I.? And you say anything other than it’s really important that we remain competitive with China and it’s really important that we have fair, transparent, unbiased systems. If you say those two, you’re like, oh, it’s great, it’s what we want. And those are really important for sure and we think a lot about those. But if you say it’s also important that we talk about 20, 30, 40, 50 years from now when we have these systems that are way more capable than any human leaving from Earth to go off and explore, and colonize the universe, and figuring out what the role for humans are and how we want to set up that society, you get a real eyes glazed over look and sort of slowly back away from.

EZRA KLEIN: Do you believe in 30 years we’re going to have self-intelligent systems going off and colonizing the universe?

SAM ALTMAN: Look, timelines are really hard. I believe that will happen someday. I think it doesn’t really matter if it’s 10 or 30 or 100 years. The fact that this is going to happen, that we’re going to help engineer, or merge with or something, our own descendants that are going to be capable of things that we literally cannot imagine. That somehow seems way more important than the tax rate or most other things.

EZRA KLEIN: But in a weird way I’m not sure it is. I mean, it is more important than the marginal tax rate on high income. I very much agree with that. But I do think sometimes there is a tendency to say that the intermediate questions between here and AGI don’t matter that much. And I think they do, because I think that they matter very much in terms of what the future systems of the world will do. I’ll give an example of this. I think there’s a lot of question on how do we distribute income, which if you could get the politics right to do it, is a quite manageable question. If you gave me the wand, I could work with five tax experts and figure it out. The question of how do you distribute dignity and status in that society —

SAM ALTMAN: 100%,

EZRA KLEIN: —is unbelievably harder. So for instance, I’m pretty high on the idea that maybe wage labor is an intermediate step in human society and wouldn’t it be great if we got past the point where it was widely needed. But that is much more a cultural question in the worlds we’re talking about here than it even is an economic one.

SAM ALTMAN: 100%. I think this is such a harder problem and in many ways more important problem than how we’re going to redistribute income and wealth. And this is why I think the intermediate things do matter a lot. It’s because how we — the steps that we take now will determine who has power and voice and input in the long-term decisions that are some of these rare, irreversible human decisions that we’ll ever make. You are probably sitting there, or at least part of you is sitting there, looking at me, thinking like, I probably don’t really believe this guy all the way. But if he’s right, fuck that dude, why does he get to decide what happens with A.I.? That’s not — that doesn’t seem fair. And you’re totally right. And if I were you, that’s totally what I would think. And more importantly than that, everybody has a right to a say in the future, and the dignity of being part of it, and getting to live their lives the way that they want. And I don’t think we’ve ever quite faced a technology like this and I don’t think we quite know what it looks like to have equitable input in those decisions.

EZRA KLEIN: And I’ll say more than that. I don’t even know if what you’re telling me is true, right? What I think is that there is a probability it is true that I cannot quite assess.

SAM ALTMAN: Right.

EZRA KLEIN: And if that probability is significant, and I think it at least is for the economic side of this — I don’t know about the space colonization side or on what time frame — then it’s important. Two things. One is that I think an endless truth of human society, at least in the age of capitalism, is that status follows money.

SAM ALTMAN: Yep.

EZRA KLEIN: And so getting the money right is going to be crucial to getting the status right, which is why the redistribution questions are really, really important. But the second then becomes, what are the governance structures that might work here, or the participatory or representative structures that might work here? Because I’ve been pushing so far in this conversation on the problems of capitalism. It isn’t like I’m confident that a state-run A.I. is a great idea too. I don’t really want China running one of these systems and I wouldn’t have wanted Donald Trump running —

SAM ALTMAN: No.

EZRA KLEIN: —one of these systems. And so the governance question here strikes me as really hard and not one where I’m comfortable with either of the dominant options.

SAM ALTMAN: I think we need something fundamentally new. We’re trying to run some experiments and do some investigatory work here. I don’t think anyone’s ever figured out what a global democratic governance system looks like. But I think we better try to figure that out soon. And there’s a lot of reason to be pessimistic. Look, I also — I think that — I think everything that I’ve said is going to happen, but we could hit some wall. It’s always possible and maybe none of this happens. But if we shift the frame a little bit and talk about — we were talking about the environment earlier, so let’s go back to that. We could have had nuclear energy deployed everywhere, the full generating capacity needed for Earth and then some, quite a long time ago. And we don’t. And I think that’s a real shame of policy, and, at least in this country, some quite bad political decisions on the left and an understandable but misplaced fear of technology. And we’re paying an awful price for it right now. And if we take all the speculation out of something like A.I. and just say can we look at an example of a collision of technology, and policy, and politics, and public perception, and economics, and a whole bunch of other things, too, and see where we got the governance wrong, we don’t need to make up examples for this. And so that is a scary thing.

EZRA KLEIN: Yeah, and that, I think, is also an important thing. I mean, we were talking earlier about, well, what if A.I. can solve in the reasonably near term — 10, 20 years — pretty big societal problems? A lot of the problems — and this came up in our conversation about health and housing. No computer system can solve a political problem, but it can create alternatives. And then we do have a lot of genuine technical and scientific problems that do need to be solved. And if we don’t get governance right, if we don’t get public input right, if people don’t feel they’re going to benefit from this, then we’re also going to delay deployment of technologies. There’s a lot of this where you’re going to need regulatory decisions for the things to be deployed. And so that becomes a question of to what degree are people comfortable with it. And not just Phoenix is going to allow self-driving taxis for a little bit to show they can. But do you actually begin to say, we are going to create the systems, the liability systems, et cetera, that can allow this to go all through society or not? And I don’t know the answer to any of that. I’m partially doing these shows for this reason that it’s just not something that I think is enough part of the political conversation. But then I look at the past year and I see a lot of failures of governance followed by a gigantic success of mRNA vaccines. And if we had not gotten that technology right, we would just be in a continued mess here. And so getting the technologies right fast enough that they can actually solve the problems, you can really see there what it would have meant if we had not — I don’t think regulators did a crazy good job on this, but we got the vaccines out.

SAM ALTMAN: I don’t think they did a crazy good or a crazy bad job on this one, but I do think they’ve done a crazy bad job on a lot of other medical innovations that could have saved a lot of lives where something has gone wrong in terms of our risk tolerance for those. Now, look, it does warm my heart that when a heroic effort is needed, we can sometimes step up. But I do think it is worth thinking about how many things like mRNA vaccines we have missed, or are still delayed, or came 10 years too late.

EZRA KLEIN: But isn’t there, in some of the things you’re talking about here, a cultural question that afflicts your own industry pretty centrally? I wouldn’t say that the people who run major technology companies are heavily anti-tax. Not in general. But there is a pretty heavy strain of the venture capitalists and others who love their carried interest tax, who get — and it’s not just the taxes — who get real angry at the idea of taxes as a moral phenomenon. That I think is an important dimension of this. Get real angry at the idea that being taxed might imply they don’t deserve what they have. There was a vote a couple of years ago where folks were comparing this to Naziism. That if this stuff is going to deploy at the rate people wanted to out here, I think there’s going to need to be a different politics in Silicon Valley.

SAM ALTMAN: I actually think that most people in the industry are pretty happy to pay taxes. Sure they may advocate for less. There’s two comments that you hear a lot, one I agree with and one that I don’t. One is that I’m happy to pay taxes, I just wish they were better spent. And because they’re so badly spent, I don’t want to pay any. While California is in shambles, why am I paying 13.3% tax? This is embarrassing. We have terrible schools, terrible roads, traffic. The money is being so wasted. I don’t want to pay anymore. And so I’m moving or I’m going to try to figure out some other tax setup or whatever. I don’t agree with that. You hear it a lot. I do understand where people are coming from. They’re like, well, I can allocate the capitol better than the government can to still help people. The one that I do agree with is I think there’s a lot of people in the tech industry — founders, venture capitalists, whatever — that really object to messaging like billionaires should not exist. Which is very different from saying billionaires shouldn’t be taxed. I would love to have trillionaires in the world if they were paying a lot of tax. And I think everybody else should want that, too. Now, there is a challenge that comes with the point you were making about a lot of power comes with that, too.

EZRA KLEIN: Yeah, that’s what I was going to ask.

SAM ALTMAN: But on the whole, as long as people are paying taxes and creating economic value, I want more of that. And I think most members of society should want more of that, too, if we can figure out how to make sure that we have fair access to power and voice and governance. And maybe what you would say is that’s not possible with that level of contribution of wealth.

EZRA KLEIN: Yeah, I would say I think there might be a more deeper tension there than you think. So take the couple of richest people in the world right now. Is it such an accident that Jeff Bezos and Bill Gates live in Seattle, a state with no income tax? It’s all fine to be for taxes in some conceptual way. But in practice, very rich, very powerful people living in a state — and it’s not like they’re helping to get an income tax passed. Or that Elon Musk just re-domiciled himself in Texas to pay, at least in part, lower taxes. I mean, power speaks. And I mean, my worry — I don’t think there should be a trillionaire. Not because I don’t want somebody to invent the thing that would have made them a trillion dollars — I do. But one, the marginal utility of having a trillion dollars is crazy low for one person. That should just be distributed to people who then won’t die from malaria because they have some money. But two, that’s a lot of power for one person to have. And I think if I have one critique of your approach to politics on this stuff it’s that I think you take policy seriously and power less seriously. But one of my observations from covering policy for a long time is policy reflects power. It doesn’t precede it.

SAM ALTMAN: I can totally believe that. again, I think if there is a big bug in my thinking, this is likely it. I’m very sympathetic to the idea of being wrong here. I doubt that it’s an accident that those people all live in no income tax states. But I also think — I haven’t talked to Elon about this, but I know him well enough that I would bet that his bigger reason was just an increasing unfriendliness in California towards his businesses and a real disagreement with how they were handling his company’s ability to be successful. And that is, I think, a real shame for all of us. No one, as California residents, none of us benefit from having fantastic companies move out of the state. That is a real shame. And that was power that the California legislature had that I think they badly misused that preceded the politics. And I wish that didn’t happen. On the trillionaire question — we were talking earlier about health care. Let’s say someone invents — some scientist invents something that gives everybody on Earth 20 years of extra great health span. And they want to make it phenomenally expensive. But they create $100 trillion of value and become a one trillionaire in the process. I would cheer them on.

EZRA KLEIN: I just don’t think that’s the binary question. It’s hard for me to imagine —

SAM ALTMAN: But then how do you decide how much they’re allowed to make?

EZRA KLEIN: I mean, through politics, right? It’s hard for me to imagine the person who would invent that, who would be dissuaded from inventing that because they would only end up with $50 billion as opposed to a trillion dollars.

SAM ALTMAN: So we’re going to say $50 billion is OK?

EZRA KLEIN: I don’t think we’re going to find an optimal. But again, I’d want to know a little bit more about both the product and the power distribution before I became comfortable with their being trillionaires because they can cause a lot of damage. And let me argue that there’s actually more of a friction here even than we’ve let on. So your point about Elon Musk is well taken. I’m not saying anything is mono-causal. But I think something going on in California in the relationship between the state and the technology companies that are centered here, and something that’s not going to be good for either side, is that as the increase in wealth inequality here rises, the sentiment changes. The politics change. And so part of the reason there’s more friction is because people are more pissed off. A different example and one that I think is in some ways easier to see the problems with is Mark Zuckerberg gives a huge amount of money to a hospital, names it after himself, and then there’s this fight and the — I think it was the board of supervisors that voted to condemn the name of the hospital. And part of what’s just going on there is people are angry about the power he has. I don’t think it was a bad thing he gave that money to the hospital. And given the way we’ve named things after people forever — I mean, go to a sports stadium around this country — I didn’t even really care that it got named after him. But there is a tension that begins to emerge and poison relations as people begin to feel that the wealth of the economy is unequally shared. And I think that’s a pretty big issue. I mean, one place my politics has probably been moving in recent years is I would like to see a much more radically pro-technology progressivism. But I think in order to do that, you might need a much more economically aggressive form of progressivism. That’s why I’m interested by the fully automated luxury communism concept, because I wonder if in order to create enough societal comfort to have the technological society I think is possible, you actually need a much more radical form of equality than we have. I did this show with Ted Chiang, the science fiction writer. He made this point where he said, I think most of our fears about technology are fears about capitalism. And I depart from that in the sense of if you live in China, or a lot of other countries, I don’t think that’s true, and even sometimes not in this country. There’s things to worry about with the state, too. But it is true for a lot of things here, and I think it actually holds back technology and the degree to which people are willing to adopt it in a way that is bad for everyone.

SAM ALTMAN: So on this point, I think we’re in perfect agreement. I think we have to do this. I think technology can make the world unimaginably great, but it needs a policy and power tweak to have that be distributed in a way where it can happen at all and in a way where it can happen justly. So I agree with that. I also agree that the heads of the biggest technology companies probably do have too much power, or do have too — I’ll take out the probably. In the Industrial Revolution, when the joint stock corporation was created as this second order sovereign entity, everyone was OK with that, because it was second order and the real sovereign had more power. But I think you can certainly make a case now that the giant tech companies are more powerful than many countries, certainly not the U.S. yet. But they don’t have any kind of democratically governed system. So yeah, I mean, that causes me deep discomfort.

[MUSIC PLAYING]

EZRA KLEIN: When I asked Ted Chiang about AGI, he said something I’ve been thinking about since. Which is that could we invent it? Maybe. Will we invent it? Maybe. Should we invent it? No. And the reason he said no was that long before we have a sentient generally intelligent A.I., we’ll have A.I. that can suffer. And if you think about how we treat animals, or even just think about how we treat computers, or, frankly, workers in many cases, the idea that we can make infinite copies of something that can suffer that we will see in a purely instrumental way is horrifying. And that fully aside from how human beings will be treated in this world, the actual A.I. will be treated really badly. Do you — I mean, you’re somebody who thinks out on the frontier of this. I know this part of the conversation is going to turn some listeners off, but I think it’s interesting. Do you worry about the suffering of what we might create?

SAM ALTMAN: Yes, a lot. And we’d call that model welfare, but it’s the same idea. Fundamentally, I think people worry are we going to mistreat the A.I. like we mistreat animals or is the A.I. going to mistreat us like with animals? That’s —

EZRA KLEIN: Yes.

SAM ALTMAN: Mistreat animals. That’s the — you can put people in one of those two buckets usually.

EZRA KLEIN: It really says a lot about how we treat animals. [LAUGHS]

SAM ALTMAN: I think we’re going to have a lot more vegetarians soon, I hope. There’s this great A.I. short story called, “Crystal Nights.” And it’s one of the ways that A.I. could be developed is what people call multi-agentally. Basically, rerun evolution and simulation. In an environment like that, you probably do get enormous amounts of suffering. A lot of other approaches I think you do, too. Maybe if a reinforcement learning agent is getting negative rewards, it’s feeling pain to some very limited degree. And if you’re running millions or billions of copies of that, creating quite a lot, that’s a real moral hazard. The technical path that I think — currently think is most likely to get us to one of these AGI-like systems is one where you don’t have tons of copies of agents. And so maybe there’s a moral issue with causing any pain. But I sleep a little bit better at night knowing that we’re not torturing trillions of agents in simulation. I also think — and this is deep into the realm of speculation — that certainly, I think, as humans have become more knowledgeable, and wise, and smarter, we seem to be less willing to inflict random pain on each other and maybe animals than we were —

EZRA KLEIN: See, I think animals is the counter-argument to that. Because of our capabilities, the number of animals we mistreat is so wildly out of proportion of what we’ve ever been able to do before, because we can keep them alive in sheds with antibiotics and stuff, that our thinking about it is probably better, but what we’re willing to outsource is worse.

SAM ALTMAN: I don’t know. I have noticed over the last few decades more and more of my friends consistently become vegetarian. I think that’s a positive. You used to not have a lot of vegetarians in the Western world. We have the privilege and luxury to be able to not do that. We now increasingly have the technology to have fake meat. But I think we also have people who are just more conscious about these issues. And I hope that we are in the late stage of the twilight of factory farming. I mean, look, we’re heading into the deepest philosophical questions that have been on humanity’s mind for a very long time, but maybe have never been as relevant or as decision-relevant as they are now. But I think a lot of these things really come down to, A, do you believe that a sense of self exists at all or is everything just like — there’s this body, and there’s this brain, and there’s energy flowing through a neural network in your head like there could be in a computer. And as that is running, it creates this illusion of a sense of self that is getting tortured but it really is not there at all and that it’s all the same thing. That’s a philosophy that I happen to mostly feel is the most true. There’s others who would say quite the opposite, which is that there will never be a sense of self in a — there is a self. There’s a soul, whatever. And that will never exist in a computer. And so all of these questions are irrelevant. There’s no way that any neural network running in Silicon could ever suffer and it’s a ridiculous question. People have quite different opinions on this.

EZRA KLEIN: Why try to make it generally intelligent at all? Geoff Hinton, one of the fathers of neural networks, he had this quote in the book “Genius Makers,” that I recently read, where he just says, why do you want the robot digging your ditches to know about baseball? Why create the potential for this kind of intelligence and kind of suffering at all? Why not just create narrow worker machine learning programs?

SAM ALTMAN: I have a lot of answers to this question, so I will start with a few. Number one, one thing that I really want is new knowledge creation. It is one thing to say you can have an A.I. that is as good as any human A.I. doctor. It is another to say you can have an A.I. that can solve all human disease in a way that humans are just not capable of doing. And I think you need a generally intelligent system to do that, to generate new knowledge, to learn new things, to do things humans can’t do. And it will need to pull together expertise across many different areas that no human is capable of holding in their brain at once — or even a team of humans — to do. So what a depressing thought to say that we’re going to limit ourselves to what humans are capable of rather than benefit from everything that we can build better tools for. We build tools so that we can do better than we can do with our hands digging up the dirt or whatever. All of this, everything we have here is because we started digging up the ground, finding stuff. And we made this room. We made this microphone. We made the internet. We have done incredible work with tools that have let us shoot past what we’d be capable of without them. And let’s not stop. That would really be depressing to me. Two is that someone’s going to do it. The upside of these systems are such that Geoff Hinton can certainly decide not to try to build generally intelligent systems, but someone’s going to do it. So I think there is no future that doesn’t have these systems in it. And so we have to talk about how we want to use them, what their rights are, what we want the world to look like, the universe to look like with them.

EZRA KLEIN: If we’re sitting — if we get together for coffee in 20 years and none of it happened, it all just stalled out, what is the likeliest reason you’re going to give me for it?

SAM ALTMAN: If it doesn’t happen in 20 years, I’ll talk about a bunch of little technical things that could go wrong. If it doesn’t happen in 100 years, then I was wrong and there is some magic to being a human like we are, living in a simulation, or created by some God or something like that. There’s something going on that is not just physics.

EZRA KLEIN: It’s that big? You think that it will — physics is going to be up for debate at that point? Because some people would say, how far it can get with neural networks pulling in data to do predictive learning. There’s just going to be a limit on that.

SAM ALTMAN: Well, here you are, though. I mean, it works for you.

EZRA KLEIN: Yeah, but only so well. You should see me — you should see me on my off days.

SAM ALTMAN: Sure. But if we can have an Ezra, that’s pretty great. And my understanding, my belief is that you are energy flowing through a neural network. That’s it. Perception comes in. It cycles around a neural network in your head and you — some muscle of yours moves. But that’s it. That’s the whole Ezra. And that is replicatable energy flowing through a neural network. And is replicable in a very big computer. It’ll take us a while to figure out there’s a lot of complexity there maybe. But yeah, if it doesn’t happen in a few hundred years, or 100 years even, then some axiom I believe is wrong.

EZRA KLEIN: I’m going to go meditate on the idea that I’m energy flowing through a neural network.

SAM ALTMAN: It is a little depressing. But if you can just let this one idea go that there’s a special self, there’s an Ezra that controls all of this. And just say, there’s nothing here. It’s just the system and it has this side effect of me thinking I’m an Ezra, then it all kind of works.

EZRA KLEIN: I think that’s a good place to end. So what are three books you’d recommend to the audience to help the energy flow slightly differently through their neural networks?

SAM ALTMAN: I would recommend — both because I think they’re more likely to get read and I think they’re more relevant to this conversation. I don’t think there’s any great books about A.I., but there are good short stories - So I would recommend short stories: “Crystal Nights” by Greg Egan, “The Last Question” by Isaac Asimov, and “The Gentle Seduction” by Marc Stiegler. They’re all about the development of a super powerful A.I. in very different ways. Actually, if I can recommend a bonus fourth one. This is a blog post, not a short story, but it really touches on a lot of this societal governance power issues we’re talking about relative to A.I. “Meditations on Moloch.” It’s a blog post on Slate Star Codex. I strongly recommend that one.
"""

def format_interview(interview_text, interviewer_name):
    lines = interview_text.strip().split("\n")
    conversations = []
    conversation = None

    for line in lines:
        # Remove text within square brackets such as [LAUGHTER] etc.
        line = re.sub(r'\[.*?\]', '', line).strip()

        if not line:
            continue

        colon_index = line.find(":")
        if colon_index == -1:
            continue

        role = "user" if interviewer_name in line[:colon_index] else "assistant"
        content = line[colon_index + 1:].strip()

        if role == "user":
            if conversation:
                conversations.append(conversation)
            conversation = {
                "messages": []
            }

        conversation["messages"].append({
            "role": role,
            "content": content
        })

    if conversation:
        conversations.append(conversation)

    return conversations

if __name__ == "__main__":
    interviewer_name = input("Enter the interviewer's name (e.g., EZRA KLEIN): ")
    formatted_data = format_interview(INTERVIEW, interviewer_name)
    output_filename = input("Enter the output filename (without .json extension): ") + ".json"
    output_path = os.path.join(output_directory, output_filename)

    with open(output_path, 'w') as outfile:
        json.dump(formatted_data, outfile, indent=4)

    print(f"Formatted interview saved to {output_path}")
