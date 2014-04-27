<div class="slides">
    <section data-background-image="https://s3.amazonaws.com/media-p.slid.es/uploads/johnschindler/images/357186/football-field.jpg" data-id="5c2ab2f8e2b8e4bcb8434f5c89be51bc">
        <h1>
            SBiDB</h1>
<p>
    <font style="font-size: 54px;" color="#f1c232">
        <b>
        <u>Inglorious Bashers</u>
    </b>
</font>
</p>
<p>
<font style="font-size: 54px;" color="#f1c232">
    <b>John Schindler&nbsp;</b>
</font>
</p>
<p>
<font style="font-size: 54px;" color="#f1c232">
    <b>&nbsp;Sophia Hernandez&nbsp;</b>
</font>
</p>
<p>
<font style="font-size: 54px;" color="#f1c232">
    <b>Trent Kan&nbsp;</b>
</font>
</p>
<p>
<font style="font-size: 54px;" color="#f1c232">
    <b>Yoan Chinique&nbsp;</b>
</font>
</p>
<p>
<font style="font-size: 54px;" color="#f1c232">
    <b>&nbsp;Sam Tipton</b>
</font>
<br>
</p>
<p>
<br>
</p>
<p>
<br>
</p>
<p>
<br>
</p>
</section>
    <section data-id="653aa4c858f79ca93fbaea8286efec58">
    <h2>
        <img src="https://s3.amazonaws.com/media-p.slid.es/uploads/samtipton/images/365513/franchises.png">
        <span style="font-size: 75.96px;">Purpose</span>
    </h2>
    <p>
    <br>
</p>
<ul>
    <li>Attractive Data Set<br>
    </li>
    <li>Reasonable Demand</li>
    <li>Personal Interest<br>
    </li>
</ul>
<p>
<br>
</p>
<p>
<br>
</p>
<img src="https://s3.amazonaws.com/media-p.slid.es/uploads/samtipton/images/365515/franchises.png">
</section>
    <section data-id="7b58492b0c5ae3db8e454fdf83557fc9">
    <h2>Overview</h2>
    <p>1. set(Data)<br>
</p>
<p>2. The Front-End<br>
</p>
<p>3.&nbsp; The Back-End<br>
</p>
<p>4. diff IngloriousBashes ITSAFEATURE<br>
</p>
<p>
<br>
</p>
</section>
    <section data-id="145f6f725790c54dceddc21a7d8b7c12">
    <section data-id="039d83d39be7837383086282656b4f5f">
        <h2>DATA</h2>
        <p>
        <br>
    </p>
    <p>
    <br>
</p>
<ol>
    <li>Our data has relationships</li>
    <li>What they represent on the site</li>
    <li>Why did we choose this particular set of relationships<br>
    </li>
</ol>
</section>
<section data-id="a6cabbc3d44f4a4206e4d7b76cf3d518">
    <h2>Title</h2>
</section>
</section>
    <section data-id="20bdf485a6265ee5a6090b959f5f9d4e">
    <section data-id="c61f52453587bbdc116a6abc46114575">
    <h2>FRONT-END</h2>
    <p>
    <br>
</p>
<p>
<br>
</p>
<ol>
    <li>Design Patterns</li>
    <li>Navigation</li>
    <li>Responsiveness</li>
    <li>External Media Integration<br>
    </li>
</ol>
</section>
    <section data-id="6213f0d69923581362d430eaac61ae6b">&nbsp;<h2 class="absolute-element" style="position: absolute; width: 364px; height: 68px; z-index: 4; left: 287px; top: 11px;">GRIDS ARE gOOD</h2>
    <img src="https://s3.amazonaws.com/media-p.slid.es/uploads/samtipton/images/365510/mvps.png" class="absolute-element visible" style="position: absolute; max-height: none; max-width: none; width: 341.499px; height: 481px; z-index: 4; left: 567px; top: 84px;" data-fragment-index="0">
    <h2>
        <br>
    </h2>
    <h2>
        <br>
    </h2>
    <h2>
        <br>
    </h2>
    <h2>
        <br>
    </h2>
    <h2>
        <br>
    </h2>
    <h2>
        <br>
    </h2>
    <p style="position: absolute; width: 541px; height: 68px; z-index: 4; left: -74px; top: 620px;" class="absolute-element fragment" data-fragment-index="0">So is Breathing Room&nbsp;</p>
    <img src="https://s3.amazonaws.com/media-p.slid.es/uploads/samtipton/images/365505/superbowls.png" style="width: 329.902px; height: 482px; max-height: none; max-width: none; position: absolute; z-index: 4; left: 18px; top: 87px;" class="absolute-element visible current-fragment" data-fragment-index="2">
</section>
<section data-id="20a7ff37cc8ff9face13acbda936801c">
    <h2>hIERARCHY</h2>
    <div>
        <br>
    </div>
</section>
</section>
    <section data-id="dbcd2757e981a46cbfec1ac65d61cff0">
    <section data-id="8f508dea79ad391bbea0cb3c141aca16">
        <h2>BACK-END</h2>
        <p>
        <br>
    </p>
    <ol>
        <li>API</li>
        <li>Analytics</li>
        <li>Search<br>
        </li>
    </ol>
</section>
<section data-id="37ae90f4951e09784e9744768aaaf5c6">
    <h2>API</h2>
    <p>
    <br>
</p>
<p>
<br>
</p>
</section>
    <section data-id="53ffde9dcb2452b26b337729a9ae0780">
        <h2>Analytics</h2>
    </section>
    <section data-id="5ebd91f2152d1fc012ef3514b8dc8e48">
        <h2>Search</h2>
        <div align="left">
            <ul>
                <li>Django-Watson</li>
                <li>Register Models in Models.py -&gt; (watson.register(SuperBowl))</li>
                <li>Take query from URL using request.GET.get('q', '') with request being the HTTP request object<br>
                </li>
                <li>If multi-word query Watson searchers returns results that include both words</li>
                <li>Split query on whitespace and search each term individually if there happens to be more than one word, then append results to the AND results from the default search performed first<br>
                </li>
            </ul>
        </div>
    </section>
</section>
    <section data-id="a2464fe6ec19a64231473af97adfc59f">
    <section data-id="66732f42d09d7decb7da8515f181a346">
        <h2> diff IngloriousBashers ITSAFEATURE</h2>
        <p>
        <br>
    </p>
    <ol>
        <li>What did we do well?</li>
        <li>What did we learn?</li>
        <li>What can we do better?</li>
        <li>What puzzles us?<br>
        </li>
    </ol>
</section>
<section data-id="4676feabc845b19696e4ea7c6ce6bf71">
    <h2>what did we do well?<br>
    </h2>
</section>
<section data-id="2835e2d55c957e2c750485f743b985b7">
    <h2>What can we do better?</h2>
    <p>Create meaningful and static URLs that a user would be able to reuse.</p>
    <p>
    <br>
</p>
<p>Keep internal state information from being revealed to the outside world. ({id})<br>
</p>
</section>
</section>
    <section data-id="54092c1c61eba09608c07124e3cccf97">
    <section data-id="173dea72f6934716c02b84da3a37fe78">
        <h2>What did they do well?<br>
        </h2>
    </section>
    <section data-id="2acd060c498cad3679dfb34d31d3fbca">
        <h2>What can they do better?</h2>
        <p>
        <br>
    </p>
</section>
</section>
    <section data-id="d6dc02979d91c907a29790f62732e780">
    <br>
</section>
    <section data-id="f7a1a2e20a439f2ec5ab528580fd7aee">
    <h2>Title</h2>
</section>
    <section data-id="d57a78fc521bc955cb6c5d97311d9e06">
    <h2>Title</h2>
</section>
</div>
