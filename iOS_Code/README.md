# How To Make An iOS App
## This tutorial will walk you through the process of making your first iOS app so you will be familiar with the Xcode IDE

> **Note** You must download Xcode to proceed with the tutorial. This is only available on Mac computers.

</section>
<section class="section">
  <a name="//apple_ref/doc/uid/TP40015214-CH5-SW3"></a>
  <h3 class="section-name" tabindex="0">Create a New Project</h3>
  <p class="para">
  Xcode includes several built-in app templates for developing common types of iOS apps, such as games, apps with tab-based navigation, and table view-based apps. Most of these templates have preconfigured interface and source code files. For this lesson, you’ll start with the most basic template: Single View Application.
</p><p class="para">
  <strong class="inline-head">To create a new project</strong>
</p><ol class="list-number">
  <li class="item"><p class="para">
  Open Xcode from the <code class="code-voice">/Applications</code> directory.
</p>
<p class="para">
  If this is the first time you’ve launched Xcode, it may ask you to agree to the user agreement and to download additional components. Follow the prompts through these screens until Xcode is completely set up and ready to launch.
</p>
<p class="para">
  As soon as Xcode launches, the welcome window appears.
</p>
<figure class="figure">
  <a name="//apple_ref/doc/uid/TP40015214-CH5-SW11"></a>
  <span class="caption"></span>
  <img width="646" alt="xcode1" src="https://user-images.githubusercontent.com/45681472/49830153-f2a8db00-fd55-11e8-907f-cbf38d20ea7f.png">
</figure>
<p class="para">
  If a project window appears instead of the welcome window, don’t worry—you probably created or opened a project in Xcode previously. Just use the menu item in the next step to create the project.
</p>
</li><li class="item"><p class="para">
  In the welcome window, click “Create a new Xcode project” (or choose File &gt; New &gt; Project).
</p>
<p class="para">
  Xcode opens a new window and displays a dialog in which you choose a template. 
</p>
</li><li class="item"><p class="para">
  Select iOS at the top of the dialog.
</p>
</li><li class="item"><p class="para">
  In the Application section, select Single View Application and then click Next.
</p>
<figure class="figure">
  <a name="//apple_ref/doc/uid/TP40015214-CH5-SW13"></a>
  <span class="caption"></span>
  <img width="672" alt="xcode2" src="https://user-images.githubusercontent.com/45681472/49830185-0e13e600-fd56-11e8-8556-523b0e5b10e4.png">
</figure>
</li><li class="item"><p class="para">
  In the dialog that appears, use the following values to name your app and choose additional options for your project:
</p>
<ul class="list-bullet">
  <li class="item"><p class="para">
  Product Name: <code class="code-voice">Dehumidifier</code> (Ignore name in image)
</p>
<p class="para">
  Xcode uses the product name you entered to name your project and the app.
</p>
</li><li class="item"><p class="para">
  Team: If this is not automatically filled in, set the team to None.
</p>
</li><li class="item"><p class="para">
  Organization Name: The name of your organization or your own name. You can leave this blank.
</p>
</li><li class="item"><p class="para">
  Organization Identifier: Your organization identifier, if you have one. If you don’t, use <code class="code-voice">com.example</code>.
</p>
</li><li class="item"><p class="para">
  Bundle Identifier: This value is automatically generated based on your product name and organization identifier.
</p>
</li><li class="item"><p class="para">
  Language: Swift
</p>
</li><li class="item"><p class="para">
  Devices: Universal
</p>
<p class="para">
  A Universal app is one that runs on both iPhone and iPad.
</p>
</li><li class="item"><p class="para">
  Use Core Data: Unselected.
</p>
</li><li class="item"><p class="para">
  Include Unit Tests: Selected.
</p>
</li><li class="item"><p class="para">
  Include UI Tests: Unselected.
</p>
</li>
</ul>
<figure class="figure">
  <a name="//apple_ref/doc/uid/TP40015214-CH5-SW14"></a>
  <span class="caption"></span>
  <img width="673" alt="xcode3" src="https://user-images.githubusercontent.com/45681472/49830208-22f07980-fd56-11e8-9007-e5044d1a76de.png">
</figure>
</li><li class="item"><p class="para">
  Click Next.
</p>
</li><li class="item"><p class="para">
  In the dialog that appears, select a location to save your project and click Create.
</p>
<p class="para">
  Xcode opens your new project in the <span class="x-name"><a href="GlossaryDefinitions.html#//apple_ref/doc/uid/TP40015214-CH12-SW9" data-renderer-version="2" data-id="//apple_ref/doc/uid/TP40015214-CH12-SW9">workspace window</a></span>.
</p>
<figure class="figure">
  <a name="//apple_ref/doc/uid/TP40015214-CH5-SW15"></a>
  <span class="caption"></span>
  <img width="619" alt="xcode4" src="https://user-images.githubusercontent.com/45681472/49830317-706ce680-fd56-11e8-9f2d-9d020e9583a5.png">
</figure>
</li>
</ol><p class="para">
  The workspace window may have an error icon with a message that says “Signing for FoodTracker requires a development team.” This warning means you haven’t set up Xcode for iOS development yet, but don’t worry, you can complete these lessons without doing that. You do not need a development team to run the app in the simulator.
</p><div class="note">
  <a name="//apple_ref/doc/uid/TP40015214-CH5-DontLinkElementID_14"></a>
  <aside class="aside">
    <p class="aside-title">Explore Further
    </p>
    	<p class="para">Before you can run the app on an iOS device, you need to set a valid team so that the app can be signed. If you are an individual or part of an organization that is a member of the Apple Developer Program, you can select that team here. Otherwise, your Apple ID is assigned to a personal team that you can use to launch apps on devices. However, you will need to join the Apple Developer Program before you can submit your app to the App store.
    	</p>
    <p class="para">
  For more information, select Help &gt; Xcode Help and search for “Signing workflow.”
</p>

  </aside>
</div>
  
</section>
<section class="section">
  <a name="//apple_ref/doc/uid/TP40015214-CH5-SW4"></a>
  <h3 class="section-name" tabindex="0">Get Familiar with Xcode</h3>
  <p class="para">
  Xcode includes everything you need to create an app. It organizes all the files and resources that go into creating an app. It provides editors for both your code and your user interfaces. Also, Xcode lets you build, run, and debug your app—providing simulators for iOS devices and a powerful integrated debugger.
</p><p class="para">
  Take a few moments to familiarize yourself with the main sections of the Xcode workspace:
</p><ul class="list-bullet">
  <li class="item"><p class="para">
  <strong class="inline-head">Navigator area.</strong> Provides quick access to the various parts of your project.
</p>
</li><li class="item"><p class="para">
  <strong class="inline-head">Editor area.</strong> Allows you to edit source code, user interfaces, and other resources.
</p>
</li><li class="item"><p class="para">
  <strong class="inline-head">Utility area.</strong> Provides information about selected items and access to ready-made resources. The Utility area is divided into two parts. The top is the <span class="x-name"><a href="GlossaryDefinitions.html#//apple_ref/doc/uid/TP40015214-CH12-SW46" data-renderer-version="2" data-id="//apple_ref/doc/uid/TP40015214-CH12-SW46">inspector pane</a></span>, where you view and edit information about items selected in the navigator or edit areas. The bottom is the <span class="x-name"><a href="GlossaryDefinitions.html#//apple_ref/doc/uid/TP40015214-CH12-SW126" data-renderer-version="2" data-id="//apple_ref/doc/uid/TP40015214-CH12-SW126">library pane</a></span>, where you access user interface elements, code snippets, and other resources.
</p>
</li><li class="item"><p class="para">
  <strong class="inline-head">Toolbar.</strong> Used to build and run your apps, view the progress of running tasks, and configure your work environment.
</p>
</li>
</ul><figure class="figure">
  
  <span class="caption"></span>
  <img width="650" alt="xcode5" src="https://user-images.githubusercontent.com/45681472/49830349-8aa6c480-fd56-11e8-8798-b21fe56d89dd.png">
</figure><p class="para">
  Don’t be overwhelmed by all of the pieces; each area is described in more detail when you need to use it.
</p>
  
</section>
<section class="section">
  <a name="//apple_ref/doc/uid/TP40015214-CH5-SW12"></a>
  <h3 class="section-name" tabindex="0">Run iOS Simulator</h3>
  <p class="para">
  Because you based your project on an Xcode template, the basic app environment is automatically set up for you. Even though you haven’t written any code, you can build and run the Single View Application template without any additional configuration.
</p><p class="para">
  To build and run your app, use the iOS <span class="x-name"><a href="GlossaryDefinitions.html#//apple_ref/doc/uid/TP40015214-CH12-SW48" data-renderer-version="2" data-id="//apple_ref/doc/uid/TP40015214-CH12-SW48">Simulator</a></span> app that’s included in Xcode. The simulator gives you an idea of how your app would look and behave if it were running on a device.
</p><p class="para">
  The simulator can model a number of different types of hardware—All the screen sizes and resolutions for both iPad and iPhone—so you can simulate your app on every device you’re developing for. In this lesson, use the iPhone 7 option.
</p><p class="para">
  <strong class="inline-head">To run your app in the simulator</strong>
</p><ol class="list-number">
  <li class="item"><p class="para">
  In the Scheme pop-up menu in the Xcode toolbar, choose iPhone 7.
</p>
<p class="para">
  The Scheme pop-up menu lets you choose which simulator or device you’d like to run your app on. Make sure you select the iPhone 7 Simulator, not an iOS device.
</p>
<figure class="figure">
  <a name="//apple_ref/doc/uid/TP40015214-CH5-SW17"></a>
  <span class="caption"></span>
  <img width="419" alt="xcode6" src="https://user-images.githubusercontent.com/45681472/49830401-ad38dd80-fd56-11e8-8c8f-8e0645735589.png">
</figure>
</li><li class="item"><p class="para">
  Click the Run button, located in the top-left corner of the Xcode toolbar.
</p>
<figure class="figure">
  <a name="//apple_ref/doc/uid/TP40015214-CH5-SW18"></a>
  <span class="caption"></span>
  <img width="689" alt="xcode7" src="https://user-images.githubusercontent.com/45681472/49830424-bf1a8080-fd56-11e8-8f7b-6955597c3724.png">
</figure>
<p class="para">
  Alternatively, choose Product &gt; Run (or press Command-R).
</p>
<p class="para">
  If you’re running an app for the first time, Xcode asks whether you’d like to enable developer mode on your Mac. Developer mode allows Xcode access to certain debugging features without requiring you to enter your password each time. Decide whether you’d like to enable developer mode and follow the prompts.
</p>
<figure class="figure">
  <a name="//apple_ref/doc/uid/TP40015214-CH5-SW19"></a>
  <span class="caption"></span>
  <img width="458" alt="xcode8" src="https://user-images.githubusercontent.com/45681472/49830458-d5c0d780-fd56-11e8-9533-09802691a4bc.png">
</figure>
<p class="para">
  If you choose not to enable developer mode, you may be asked for your password later on. These lessons assume developer mode is enabled.
</p>
</li><li class="item"><p class="para">
  Watch the Xcode toolbar as the build process completes.
</p>
<p class="para">
  Xcode displays messages about the build process in the <span class="x-name"><a href="GlossaryDefinitions.html#//apple_ref/doc/uid/TP40015214-CH12-SW24" data-renderer-version="2" data-id="//apple_ref/doc/uid/TP40015214-CH12-SW24">activity viewer</a></span>, which is in the middle of the toolbar.
</p>
</li>
</ol><p class="para">
  After Xcode finishes building your project, the simulator starts automatically. It may take a few moments to start up the first time.
</p><p class="para">
  The simulator opens in the iPhone mode you specified and then launches your app. Initially, the simulator displays your app’s launch screen, and then it transitions to your app’s main interface. In an unmodified Single View Application template, the launch screen and the main interface are identical.
</p><figure class="figure">
  <a name="//apple_ref/doc/uid/TP40015214-CH5-SW21"></a>
  <span class="caption"></span>
  <img width="388" alt="xcode9" src="https://user-images.githubusercontent.com/45681472/49830486-ebce9800-fd56-11e8-9408-572e12abaf63.png">
</figure><p class="para">
  Right now, the Single View Application template doesn’t do much—it just displays a white screen. Other templates have more complex behavior. It’s important to understand a template’s uses before you extend it to make your own app. Running your app in the simulator with no modifications is a good way to start developing that understanding.
</p><p class="para">
  Quit the simulator by choosing Simulator &gt; Quit Simulator (or pressing Command-Q).
</p>
  
</section>
<section class="section">
  <a name="//apple_ref/doc/uid/TP40015214-CH5-SW5"></a>
  <h3 class="section-name" tabindex="0">Review the Source Code</h3>
  <p class="para">
  The Single View Application template comes with a few source code files that set up the app environment. First, take a look at the <code class="code-voice">AppDelegate.swift</code> file.
</p><p class="para">
  <strong class="inline-head">To look at the AppDelegate.swift source file</strong>
</p><ol class="list-number">
  <li class="item"><p class="para">
  Make sure the project navigator is open in the navigator area.
</p>
<p class="para">
  The <span class="x-name"><a href="GlossaryDefinitions.html#//apple_ref/doc/uid/TP40015214-CH12-SW57" data-renderer-version="2" data-id="//apple_ref/doc/uid/TP40015214-CH12-SW57">project navigator</a></span> displays all the files in your project. If the project navigator isn’t open, click the leftmost button in the navigator selector bar. (Alternatively, choose View &gt; Navigators &gt; Show Project Navigator.)
</p>
<figure class="figure">
  <a name="//apple_ref/doc/uid/TP40015214-CH5-SW22"></a>
  <span class="caption"></span>
  <img width="505" alt="xcode10" src="https://user-images.githubusercontent.com/45681472/49830519-ff79fe80-fd56-11e8-9f35-924698d1cb54.png">
</figure>
</li><li class="item"><p class="para">
  If necessary, open the FoodTracker folder in the project navigator by clicking the disclosure triangle next to it.
</p>
</li><li class="item"><p class="para">
  Select <code class="code-voice">AppDelegate.swift</code>.
</p>
<p class="para">
  Xcode opens the source file in the main editor area of the window.
</p>
<figure class="figure">
  <a name="//apple_ref/doc/uid/TP40015214-CH5-SW23"></a>
  <span class="caption"></span>
  <img width="640" alt="xcode11" src="https://user-images.githubusercontent.com/45681472/49830630-5e3f7800-fd57-11e8-87a2-186983da9c56.png">
</figure>
<p class="para">
  Alternatively, double-click the <code class="code-voice">AppDelegate.swift</code> file to open it in a separate window.
</p>
</li>
</ol>
  <section class="section">
  <a name="//apple_ref/doc/uid/TP40015214-CH5-SW24"></a>
  <h3 class="section-name" tabindex="0">The App Delegate Source File</h3>
  <p class="para">
  The <code class="code-voice">AppDelegate.swift</code> source file has two primary functions:
</p><ul class="list-bullet">
  <li class="item"><p class="para">
  It defines your <code class="code-voice">AppDelegate</code> class. The <span class="x-name"><a href="GlossaryDefinitions.html#//apple_ref/doc/uid/TP40015214-CH12-SW27" data-renderer-version="2" data-id="//apple_ref/doc/uid/TP40015214-CH12-SW27">app delegate</a></span> creates the window where your app’s content is drawn and provides a place to respond to state transitions within the app. 
</p>
</li><li class="item"><p class="para">
  It creates the <span class="x-name"><a href="GlossaryDefinitions.html#//apple_ref/doc/uid/TP40015214-CH12-SW37" data-renderer-version="2" data-id="//apple_ref/doc/uid/TP40015214-CH12-SW37">entry point</a></span> to your app and a <span class="x-name"><a href="GlossaryDefinitions.html#//apple_ref/doc/uid/TP40015214-CH12-SW61" data-renderer-version="2" data-id="//apple_ref/doc/uid/TP40015214-CH12-SW61">run loop</a></span> that delivers input events to your app. This work is done by the <code class="code-voice">UIApplicationMain</code> attribute  (<code class="code-voice">@UIApplicationMain</code>), which appears toward the top of the file. 
</p>
<p class="para">
  Using the <code class="code-voice">UIApplicationMain</code> attribute is equivalent to calling the <code class="code-voice">UIApplicationMain</code> function and passing your <code class="code-voice">AppDelegate</code> class’s name as the name of the delegate class. In response, the system creates an <span class="x-name"><a href="GlossaryDefinitions.html#//apple_ref/doc/uid/TP40015214-CH12-SW75" data-renderer-version="2" data-id="//apple_ref/doc/uid/TP40015214-CH12-SW75">application object</a></span>. The application object is responsible for managing the life cycle of the app. The system also creates an instance of your <code class="code-voice">AppDelegate</code> class, and assigns it to the application object. Finally, the system launches your app.
</p>
</li>
</ul><p class="para">
  The <code class="code-voice">AppDelegate</code> class is automatically created whenever you create a new project. Unless you are doing something highly unusual, you should use this class provided by Xcode to initialize your app and respond to app-level events. The <code class="code-voice">AppDelegate</code> class adopts the <code class="code-voice">UIApplicationDelegate</code> protocol. This protocol defines a number of methods you use to set up your app, to respond to the app’s state changes, and to handle other app-level events.
</p><p class="para">
  The <code class="code-voice">AppDelegate</code> class contains a single property: <code class="code-voice">window</code>. 
</p><section class="code-listing">
  
  <div class="code-sample">
      <div class="Swift">
        <ol class="code-lines">
            <li><code class="code-voice"><span class="kt">var</span> <span class="vc">window</span>: <span class="n"><!-- a href="" -->UIWindow<!-- /a --></span>?</code></li>
        </ol>
      </div>
  </div>
</section><p class="para">
  This property stores a reference to the app’s window. This window represents the root of your app’s view hierarchy. It is where all of your app content is drawn. Note that the window property is an <span class="x-name"><a href="GlossaryDefinitions.html#//apple_ref/doc/uid/TP40015214-CH12-SW11" data-renderer-version="2" data-id="//apple_ref/doc/uid/TP40015214-CH12-SW11">optional</a></span>, which means it may have no value (be <span class="x-name"><a href="GlossaryDefinitions.html#//apple_ref/doc/uid/TP40015214-CH12-SW5" data-renderer-version="2" data-id="//apple_ref/doc/uid/TP40015214-CH12-SW5">nil</a></span>) at some point.
</p><p class="para">
  The <code class="code-voice">AppDelegate</code> class also contains stub implementations of the following delegate <span class="x-name"><a href="GlossaryDefinitions.html#//apple_ref/doc/uid/TP40015214-CH12-SW12" data-renderer-version="2" data-id="//apple_ref/doc/uid/TP40015214-CH12-SW12">methods</a></span>: 
</p><section class="code-listing">
  
  <div class="code-sample">
      <div class="Swift">
        <ol class="code-lines">
            <li><code class="code-voice"><span class="kt">func</span> <span class="vc">application</span>(<span class="kt">_</span> <span class="vc">application</span>: <span class="n"><!-- a href="" -->UIApplication<!-- /a --></span>, <span class="vc">didFinishLaunchingWithOptions</span> <span class="vc">launchOptions</span>: [<span class="n"><!-- a href="" -->UIApplicationLaunchOptionsKey<!-- /a --></span>: <span class="kt">Any</span>]?) -&gt; <span class="n"><!-- a href="" -->Bool<!-- /a --></span></code></li>
            <li><code class="code-voice"><span class="kt">func</span> <span class="vc">applicationWillResignActive</span>(<span class="kt">_</span> <span class="vc">application</span>: <span class="n"><!-- a href="" -->UIApplication<!-- /a --></span>)</code></li>
            <li><code class="code-voice"><span class="kt">func</span> <span class="vc">applicationDidEnterBackground</span>(<span class="kt">_</span> <span class="vc">application</span>: <span class="n"><!-- a href="" -->UIApplication<!-- /a --></span>)</code></li>
            <li><code class="code-voice"><span class="kt">func</span> <span class="vc">applicationWillEnterForeground</span>(<span class="kt">_</span> <span class="vc">application</span>: <span class="n"><!-- a href="" -->UIApplication<!-- /a --></span>)</code></li>
            <li><code class="code-voice"><span class="kt">func</span> <span class="vc">applicationDidBecomeActive</span>(<span class="kt">_</span> <span class="vc">application</span>: <span class="n"><!-- a href="" -->UIApplication<!-- /a --></span>)</code></li>
            <li><code class="code-voice"><span class="kt">func</span> <span class="vc">applicationWillTerminate</span>(<span class="kt">_</span> <span class="vc">application</span>: <span class="n"><!-- a href="" -->UIApplication<!-- /a --></span>)</code></li>
        </ol>
      </div>
  </div>
</section><p class="para">
  These methods let the application object communicate with the app delegate. During an app state transition—for example, app launch, transitioning to the background, and app termination—the application object calls the corresponding delegate method, giving your app an opportunity to respond. You don’t need to do anything special to make sure these methods get called at the correct time—the application object handles that job for you.
</p><p class="para">
  Each of the delegate methods has a default behavior. If you leave the template implementation empty or delete it from your <code class="code-voice">AppDelegate</code> class, you get the default behavior whenever that method is called. Alternatively, you can add your own code to the stub methods, defining custom behaviors that are executed when the methods are called.
</p><p class="para">
  The template also provides comments for each of the stub methods. These comments describe how these methods can be used by your app. You can use the stub methods and comments as a blueprint for designing many common app-level behaviors.
</p><p class="para">
  In this lesson, you won’t be using any custom app delegate code, so you don’t have to make any changes to the <code class="code-voice">AppDelegate.swift</code> file.
</p>
  
</section>
<section class="section">
  <a name="//apple_ref/doc/uid/TP40015214-CH5-SW25"></a>
  <h3 class="section-name" tabindex="0">The View Controller Source File</h3>
  <p class="para">
  The Single View Application template has another source code file: <code class="code-voice">ViewController.swift</code>. Select <code class="code-voice">ViewController.swift</code> in the project navigator to view it.
</p><figure class="figure">
  <a name="//apple_ref/doc/uid/TP40015214-CH5-SW26"></a>
  <span class="caption"></span>
  <img width="629" alt="xcode12" src="https://user-images.githubusercontent.com/45681472/49830664-6f888480-fd57-11e8-914a-017ee2abbf4f.png">
</figure><p class="para">
  This file defines a custom <span class="x-name"><a href="GlossaryDefinitions.html#//apple_ref/doc/uid/TP40015214-CH12-SW14" data-renderer-version="2" data-id="//apple_ref/doc/uid/TP40015214-CH12-SW14">subclass</a></span> of <code class="code-voice">UIViewController</code> named <code class="code-voice">ViewController</code>. Right now, this class simply inherits all the behavior defined by <code class="code-voice">UIViewController</code>. To override or extend that behavior, you override the methods defined on <code class="code-voice">UIViewController</code>.
</p><p class="para">
  As you can see in the <code class="code-voice">ViewController.swift</code> file, the template’s implementation overrides both the <code class="code-voice">viewDidLoad()</code> and <code class="code-voice">didReceiveMemoryWarning()</code> methods; however, the template’s stub implementation doesn’t do anything yet, except call the <code class="code-voice">UIViewController</code> version of these methods. You can add your own code to customize the view controller’s response to these events.
</p><p class="para">
  Although the template comes with the <code class="code-voice">didReceiveMemoryWarning()</code> method, you won’t need to implement it in these lessons, so go ahead and delete it.
</p><p class="para">
  At this point, your <code class="code-voice">ViewController.swift</code> code should look something like this:
</p><section class="code-listing">
  
  <div class="code-sample">
      <div class="Swift">
        <ol class="code-lines">
            <li><code class="code-voice"><span class="kt">import</span> <span class="vc">UIKit</span></code></li>
            <li><code class="code-voice"> </code></li>
            <li><code class="code-voice"><span class="kt">class</span> <span class="vc">ViewController</span>: <span class="n"><!-- a href="" -->UIViewController<!-- /a --></span> {</code></li>
            <li><code class="code-voice">    </code></li>
            <li><code class="code-voice">    <span class="kt">override</span> <span class="kt">func</span> <span class="vc">viewDidLoad</span>() {</code></li>
            <li><code class="code-voice">        <span class="kt">super</span>.<span class="vc">viewDidLoad</span>()</code></li>
            <li><code class="code-voice">        <span class="c">// Do any additional setup after loading the view, typically from a nib.</span></code></li>
            <li><code class="code-voice">    }</code></li>
            <li><code class="code-voice">    </code></li>
            <li><code class="code-voice">}</code></li>
        </ol>
      </div>
  </div>
</section><p class="para">
  You’ll start writing code in this source code file later in this lesson.
</p>
  
</section>

</section>
<section class="section">
  <a name="//apple_ref/doc/uid/TP40015214-CH5-SW10"></a>
  <h3 class="section-name" tabindex="0">Open Your Storyboard</h3>
  <p class="para">
  You’re ready to start working on a storyboard for your app. A <span class="x-name"><a href="GlossaryDefinitions.html#//apple_ref/doc/uid/TP40015214-CH12-SW8" data-renderer-version="2" data-id="//apple_ref/doc/uid/TP40015214-CH12-SW8">storyboard</a></span> is a visual representation of the app’s user interface, showing screens of content and the transitions between them. You use storyboards to lay out the flow—or story—that drives your app. You see exactly what you&#39;re building while you’re building it, get immediate feedback about what’s working and what’s not, and make instantly visible changes to your user interface.
</p><p class="para">
  <strong class="inline-head">To open your storyboard</strong>
</p><ul class="list-bullet">
  <li class="item"><p class="para">
  In the project navigator, select <code class="code-voice">Main.storyboard</code>.
</p>
<p class="para">
  Xcode opens the storyboard in <span class="x-name"><a href="GlossaryDefinitions.html#//apple_ref/doc/uid/TP40015214-CH12-SW47" data-renderer-version="2" data-id="//apple_ref/doc/uid/TP40015214-CH12-SW47">Interface Builder</a></span>—its visual interface editor—in the editor area. The background of the storyboard is the <span class="x-name"><a href="GlossaryDefinitions.html#//apple_ref/doc/uid/TP40015214-CH12-SW6" data-renderer-version="2" data-id="//apple_ref/doc/uid/TP40015214-CH12-SW6">canvas</a></span>. You use the canvas to add and arrange user interface elements.
</p>
<figure class="figure">
  
  <span class="caption"></span>
  <img width="630" alt="xcode13" src="https://user-images.githubusercontent.com/45681472/49830688-7fa06400-fd57-11e8-9af5-36d8fc737abc.png">
</figure>
</li>
</ul><p class="para">
  At this point, the storyboard in your app contains one <span class="x-name"><a href="GlossaryDefinitions.html#//apple_ref/doc/uid/TP40015214-CH12-SW62" data-renderer-version="2" data-id="//apple_ref/doc/uid/TP40015214-CH12-SW62">scene</a></span>, which represents a screen of content in your app. The arrow that points to the left side of the scene on the canvas is the <span class="x-name"><a href="GlossaryDefinitions.html#//apple_ref/doc/uid/TP40015214-CH12-SW66" data-renderer-version="2" data-id="//apple_ref/doc/uid/TP40015214-CH12-SW66">storyboard entry point</a></span>, which means that this scene is loaded first when the app starts. This scene contains a single view that’s managed by a view controller. You’ll learn more about the roles of views and view controllers soon.
</p><p class="para">
  When you ran your app in the iPhone 7 Simulator app, the view in this scene is what you saw on the device screen. However, the scene on the canvas may not have the same dimensions as the simulator’s screen. You can select the screen size and orientation at the bottom of the canvas. In this case, it’s set to iPhone 7 in a portrait orientation, so the canvas and the simulator are the same.
</p><p class="para">
  Even though the canvas shows a specific device and orientation, it is important to create an <span class="x-name"><a href="GlossaryDefinitions.html#//apple_ref/doc/uid/TP40015214-CH12-SW25" data-renderer-version="2" data-id="//apple_ref/doc/uid/TP40015214-CH12-SW25">adaptive interface</a></span>—an interface that automatically adjusts so that it looks good on any device and in any orientation. As you develop your interface, you can change the canvas’s view, letting you see how your interface adapts to different size screens.
</p>  
</section>


## You are nbow ready to import the files from this directory into your Dehumidifier Project
