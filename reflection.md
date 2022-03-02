Reflect on which controls worked well for the games and which did not. Why do you think this is? Where did some 
fall short in terms of our five interaction rules? 

Introduction:
    For this project, we implemented 5 different ways to control a game (for example either the snake game or Pacman). For 
    the purposes of this reflection, we will discuss our experience with the snake game, which we used to test our
    implementations of the different controls. The controls we implemented were the following: key press, trackpad,
    color tracking, finger detection and voice control. Throughout our testing of these different controls, we noticed
    significant differences in both their efficiencies and convenience, which we'll discuss in further detail below. We'll 
    also analyze each control's adherence to the five interaction rules, which are: Thinking through doing, Performance, 
    Visibility, Risk, and Thickness of Practice.

    As a reminder, the five interaction rules refer to the following ideas:
        Thinking through doing - Immersing oneself in the physical world as a way of learning and
            alleviating cognitive load through use of gestures
        Performance - Controls that extend our bodies in order to make interactions more efficient
        Visibility - Interactions that better mimic the task they are intended to complete
        Risk - The way people interact with things is informed by visible consequences
        Thickness of Practice - Defining characteristics of things we interact with in the physical world are lost in the process of
            digitalization.

Key press:
    We implemented the keypress control by allowing the user to control the game by using the T,H,G and F keys, sort of
    like the more common implementation of using the W,A,S,D keys as a substitute for the arrow keys. In terms of being
    able to control the snake game, we found that this game control was both the easiest to implement and the most
    convenient and efficient way to play the game. The key press game control is therefore one of the most widespread and popular
    game controls that we know. One disadvantage of the keys we selected for this game control are less ergonomically optimal than the
    arrow keys. This is because a user can use the arrow keys to control a game, while resting their hand without pressing any other
    keys on accident. In terms of the five interaction rules, this game control adheres to performance and visibility in some ways, 
    because in order to press the keys your fingers have to move in the direction that you want the object to move in. This sort of 
    also plays into the notion of 'thinking through doing' because your body mimics the direction that your head thinks the snake
    should move in.

Trackpad:
    The next control we implemented was the trackpad control, which works by having the user swipe on the trackpad in the direction
    they want the snake to move. Some challenges we faced here was determining the appropriate length of the swipe for changing the
    direction of the snake. Although we reached what we believe to be the best solution, this game control is significantly less
    user-friendly than the key press in our opinion. One of our major problems with this control is that when you swipe on the trackpad,
    you are moving the mouse but the mouse then doesn't rebound to its original location on the screen. This means if you are 
    too close to the edge of the screen with your mouse, you have to move it back which not only requires additional time and effort,
    but is sometimes misinterpreted by the game as an additional swipe. Consequently, we found it quite difficult to succeed at this
    game using this control, although not impossible. In terms of the five interaction rules, this control also adhered to thinking
    through doing, performance, and visibility. Since we programmed this control so the direction of your swipe corresponds with the
    direction in which you want the snake to move, the game control is relatively efficient and intuitive. This significantly
    alleviates cognitive load, because the user just has to mimic where they want the snake to go and the control is sort of like an
    extension of our bodies in that we are quite literally telling the snake directly where we want it to move. Although this control
    has potential as being a really effective way to interact with the game, because it is very intuitive especially for the younger
    generations who have much more experience with touchscreens and the touchpad-like method of interacting with games, something
    would have to be done to allow the mouse to rebound to its original location after a swipe.

Color tracking:
    The third control for this game is the color control, which allows the user to use an object of a specified colour (green in our case)
    to control the game. This control takes in video input and allows the user to control the snake in this way. At first, we as a group
    faced some difficulties in implementing this control due to issues with getting the colour to be appropriately recognized. After
    working with different shade allowances, we believe our solution is now relatively effective at working even in differing 
    lighting. As such, when the control is working, it is relatively similar to the trackpad. This is because we faced this similar problem
    of having to rebound the colour object back to a central location within the video frame, which was often misunderstood by
    the control as a swipe in a certain direction. So for instance, if you swipe to the right with the colour object but then are too far
    right in the video frame and have to move your colour object back into the video frame (back to the left) the game might interpret
    this as a swipe to the left. In a way, this game control requires two movements for every intended direction change - one indicating
    the actual direction you want the snake to move in and one where you bring the colour object back into the frame to be ready for the
    next move. Not only is this inefficient, but it can also be really hard to keep up with a high speed game because your head gets
    confused on which gesture is an intended directional change and which one is a rebound. In terms of the interaction rules, this
    game control is a great example of performance, because it extends our hands and allows us to sort of perform the way in which
    we want the game to behave. Additionally, the way in which this game control requires the user to use a significant part of their body
    to control the game (lifting your arm, moving your hand or your entire arm, etc.) aligns with the interaction technique of thinking
    through doing and immersing oneself in the physical world. This control also emphasizes the difference in immersion between this control
    and a much less involved control like the key press one, showing how digitization has made the way we play games much less immersive
    and much less of a full body experience.

Finger detection:
    The fourth control we implemented was one in which the user had to raise a certain amount of fingers to make the game move in a 
    certain direction. Much like the keypress, this game control is more static and consists only of a single symbol or indication of
    the user's intended control. In contrast, the other two (trackpad and color tracking) were controls that required some mimicking movement
    from the user - a swipe. Although this game control was really exciting to implement, especially as we started to understand how
    the video frame could be processes to actually detect a user's hand, it was the least intuitive of the game controls that we 
    implemented. The options for changing the game's direction are either holding up one, two, three or four fingers, to which we 
    arbitrarily assigned corresponding directions. This game control worked well in terms of efficiency of processing, however there 
    was a significant learning curve to memorizing which direction corresponded to how many fingers. This means that this control is not
    very intuitive and we think people would prefer other static controls the key press over it because those are much more intuitive. In
    terms of the five interaction rules, this control seems to violate more of them than the other controls we had implemented so far.
    For example, we don't feel as though this control aligns with performance because holding up fingers to indicate a direction does not
    seem like a natural extension of our bodies. If the control instead was to point your finger in the direction you wanted to go or
    even swipe your finger in the direction you wanted to go, this would align much better with performance. This same argument goes for
    visibility, thinking through doing, in our opinion. 

Voice control:
    When selecting which unique control we wanted to implement, we aimaed to find something that was more intuitive than some of the
    other controls we'd implemented thus far. As a result, we landed on the idea of voice control, specifically a control in which the user
    had to say the direction they wanted the game (the snake in our case) to move in. To our surprise, this control was not very difficult
    to implement, due to existing Python packages and libraries. One thing we did find with this control is that it is extremely slow and
    inefficient. As a result, this particular control (at least how we've implemented it) does not operate fast enough to be sufficient
    to control a game like the snake game. One major benefit of this control in our opinion though is the fact that it is highly 
    intuitive. It does not require any conversion or memorization to simply say which direction you want the game to move in. This is
    different than the finger detection, where you have to memorize the corresponding direction for each finger. In terms of the five
    interaction rules, we felt as though this control best corresponded through performance - verbalizing the outcome you want to see in the game.
    As well as visibility, because the direction you say mimics the direction you want to see the snake moving in. In order to improve
    this game control, we would need to determine the best way to make it more efficient.

Conclusion:
    In our group, completing this project also brought up considerations of other topics we had discussed in class. Specifically for 
    our unique control, as we were brainstorming the topic of accessibility was on the forefront of our minds. We discussed how someone
    who may not be able to interact with a snake game in the traditional sense might be able to play the game regardless. This is how
    we ended up landing on audio input, because this couuld be an alternative game control that significantly opens up the
    accessibility of a lot of games similar to the snake game. This project brought to light the importance of considering a wide
    variety of options for how to implement the controls of different games, and how important it is that companies thoroughly study this
    in order to make games customizable for accessiblity purposes. 