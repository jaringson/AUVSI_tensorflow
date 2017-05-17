<!DOCTYPE html>
<html lang='en'>
<head prefix='og: http://ogp.me/ns#'>
<meta charset='utf-8'>
<meta content='IE=edge' http-equiv='X-UA-Compatible'>
<meta content='object' property='og:type'>
<meta content='GitLab' property='og:site_name'>
<meta content='vgg16.py · master · Gary Ellingson / im2att_tf' property='og:title'>
<meta content='tensorflow stuff for my Image2Attitude project' property='og:description'>
<meta content='https://magiccvs.byu.edu/gitlab/assets/gitlab_logo-cdf021b35c4e6bb149e26460f26fae81e80552bc879179dd80e9e9266b14e894.png' property='og:image'>
<meta content='https://magiccvs.byu.edu/gitlab/gellings/im2att_tf/blob/master/vgg16.py' property='og:url'>
<meta content='summary' property='twitter:card'>
<meta content='vgg16.py · master · Gary Ellingson / im2att_tf' property='twitter:title'>
<meta content='tensorflow stuff for my Image2Attitude project' property='twitter:description'>
<meta content='https://magiccvs.byu.edu/gitlab/assets/gitlab_logo-cdf021b35c4e6bb149e26460f26fae81e80552bc879179dd80e9e9266b14e894.png' property='twitter:image'>

<title>vgg16.py · master · Gary Ellingson / im2att_tf · GitLab</title>
<meta content='tensorflow stuff for my Image2Attitude project' name='description'>
<link rel="shortcut icon" type="image/x-icon" href="/gitlab/assets/favicon-075eba76312e8421991a0c1f89a89ee81678bcde72319dd3e8047e2a47cd3a42.ico" />
<link rel="stylesheet" media="all" href="/gitlab/assets/application-8465c29e28ae0d6fefb4bdb69a617dc3329e1b76b414d41274f5adda06d40a30.css" />
<link rel="stylesheet" media="print" href="/gitlab/assets/print-6939eb32d7a168d8fe54b11c4873498ba343870a6f7d2eb15147f7035a0154e2.css" />
<script src="/gitlab/assets/application-82d6c3d401eb9ebe12a24ba76e634198ed71aa30b787a764b7a8cf6a24840f34.js"></script>
<meta name="csrf-param" content="authenticity_token" />
<meta name="csrf-token" content="cWRDl0rBLnokaelnSaIP2MIo2NOkINmlwz3CBlZ6O91EkUcv+gDOaJ1NxNazgEpK+DGLHqieL5TLy4FNxQtdVQ==" />
<script>
//<![CDATA[
window.gon={};gon.api_version="v3";gon.default_avatar_url="https://magiccvs.byu.edu/gitlab/assets/no_avatar-07eeb128b993e74003e8664cff0b8e1e7234cec0443766a6763df32ca3472c23.png";gon.default_issues_tracker="gitlab";gon.max_file_size=10;gon.relative_url_root="/gitlab";gon.user_color_scheme="white";gon.current_user_id=5;gon.api_token="fd7X5GHi4pqxGSBgb7_W";
//]]>
</script>
<meta content='origin-when-cross-origin' name='referrer'>
<meta content='width=device-width, initial-scale=1, maximum-scale=1' name='viewport'>
<meta content='#474D57' name='theme-color'>
<link rel="apple-touch-icon" type="image/x-icon" href="/gitlab/assets/touch-icon-iphone-2d64ecc33893baab71adc15ff19a803a59911cc2651fb9d4d62af1379ff89aab.png" />
<link rel="apple-touch-icon" type="image/x-icon" href="/gitlab/assets/touch-icon-ipad-d08897d57e1bc9400024ac15465340e832a8e7b166b91624138d48ea2c739596.png" sizes="76x76" />
<link rel="apple-touch-icon" type="image/x-icon" href="/gitlab/assets/touch-icon-iphone-retina-81446c57f3351d1dacd0fb5f23ced74ba63d3878810bedea343999c6a12b3915.png" sizes="120x120" />
<link rel="apple-touch-icon" type="image/x-icon" href="/gitlab/assets/touch-icon-ipad-retina-e2a776da039936ac240e76615add47b25ab77c75a5fa2d1b3907f83d5502b911.png" sizes="152x152" />
<link color='rgb(226, 67, 41)' href='/gitlab/assets/logo-d36b5212042cebc89b96df4bf6ac24e43db316143e89926c0db839ff694d2de4.svg' rel='mask-icon'>
<meta content='/gitlab/assets/msapplication-tile-49c9c46afd2ab9bbf35e69138bc62f8c31fa55584bd494956ac6e58e6aadc813.png' name='msapplication-TileImage'>
<meta content='#30353E' name='msapplication-TileColor'>




<style>
  [data-user-is] {
    display: none !important;
  }
  
  [data-user-is="5"] {
    display: block !important;
  }
  
  [data-user-is="5"][data-display="inline"] {
    display: inline !important;
  }
  
  [data-user-is-not] {
    display: block !important;
  }
  
  [data-user-is-not][data-display="inline"] {
    display: inline !important;
  }
  
  [data-user-is-not="5"] {
    display: none !important;
  }
</style>

</head>

<body class='ui_charcoal' data-page='projects:blob:show'>
<script>
  window.project_uploads_path = "/gitlab/gellings/im2att_tf/uploads";
  window.markdown_preview_path = "/gitlab/gellings/im2att_tf/markdown_preview";
</script>

<header class='header-collapsed navbar navbar-fixed-top navbar-gitlab'>
<div class='container-fluid'>
<div class='header-content'>
<button class='navbar-toggle' type='button'>
<span class='sr-only'>Toggle navigation</span>
<i class="fa fa-bars"></i>
</button>
<div class='navbar-collapse collapse'>
<ul class='nav navbar-nav'>
<li class='hidden-sm hidden-xs'>
<div class='search'>
<form class="navbar-form pull-left" action="/gitlab/search" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" />
<input type="search" name="search" id="search" placeholder="Search" class="search-input form-control" spellcheck="false" tabindex="1" />
<input type="hidden" name="group_id" id="group_id" />
<input type="hidden" name="project_id" id="project_id" value="169" />
<input type="hidden" name="search_code" id="search_code" value="true" />
<input type="hidden" name="repository_ref" id="repository_ref" value="master" />

<div class='search-autocomplete-opts hide' data-autocomplete-path='/gitlab/search/autocomplete' data-autocomplete-project-id='169' data-autocomplete-project-ref='master'></div>
</form>

</div>
<script>
  $('.search-input').on('keyup', function(e) {
    if (e.keyCode == 27) {
      $('.search-input').blur();
    }
  });
</script>

</li>
<li class='visible-sm visible-xs'>
<a title="Search" data-toggle="tooltip" data-placement="bottom" data-container="body" href="/gitlab/search"><i class="fa fa-search"></i>
</a></li>
<li>
<a title="Todos" data-toggle="tooltip" data-placement="bottom" data-container="body" href="/gitlab/dashboard/todos"><span class='badge todos-pending-count'>
4
</span>
</a></li>
<li>
<a title="New project" data-toggle="tooltip" data-placement="bottom" data-container="body" href="/gitlab/projects/new"><i class="fa fa-plus fa-fw"></i>
</a></li>
<li>
<a class="logout" title="Sign out" data-toggle="tooltip" data-placement="bottom" data-container="body" rel="nofollow" data-method="delete" href="/gitlab/users/sign_out"><i class="fa fa-sign-out"></i>
</a></li>
</ul>
</div>
<h1 class='title'><a href="/gitlab/u/gellings">Gary Ellingson</a> / <a class="project-item-select-holder" href="/gitlab/gellings/im2att_tf">im2att_tf<input type="hidden" name="project_path" id="project_path" class="project-item-select js-projects-dropdown ajax-project-select" data-include-groups="false" data-order-by="last_activity_at" /></a><i class="fa fa-chevron-down dropdown-toggle-caret js-projects-dropdown-toggle"></i> &middot; <a href="/gitlab/gellings/im2att_tf/tree/master">Files</a></h1>
</div>
</div>
</header>

<script>
  var findFileURL = "/gitlab/gellings/im2att_tf/find_file/master";
</script>

<div class='page-sidebar-collapsed page-with-sidebar'>


<div class='nicescroll sidebar-collapsed sidebar-wrapper'>
<div class='header-logo'>
<a id='logo'>
<svg width="36" height="36" id="tanuki-logo">
  <path id="tanuki-right-ear" class="tanuki-shape" fill="#e24329" d="M2 14l9.38 9v-9l-4-12.28c-.205-.632-1.176-.632-1.38 0z"/>
  <path id="tanuki-left-ear" class="tanuki-shape" fill="#e24329" d="M34 14l-9.38 9v-9l4-12.28c.205-.632 1.176-.632 1.38 0z"/>
  <path id="tanuki-nose" class="tanuki-shape" fill="#e24329" d="M18,34.38 3,14 33,14 Z"/>
  <path id="tanuki-right-eye" class="tanuki-shape" fill="#fc6d26" d="M18,34.38 11.38,14 2,14 6,25Z"/>
  <path id="tanuki-left-eye" class="tanuki-shape" fill="#fc6d26" d="M18,34.38 24.62,14 34,14 30,25Z"/>
  <path id="tanuki-right-cheek" class="tanuki-shape" fill="#fca326" d="M2 14L.1 20.16c-.18.565 0 1.2.5 1.56l17.42 12.66z"/>
  <path id="tanuki-left-cheek" class="tanuki-shape" fill="#fca326" d="M34 14l1.9 6.16c.18.565 0 1.2-.5 1.56L18 34.38z"/>
</svg>

</a>
<a class="gitlab-text-container-link" title="Dashboard" id="js-shortcuts-home" href="/gitlab/"><div class='gitlab-text-container'>
<h3>GitLab</h3>
</div>
</a></div>
<ul class='nav nav-sidebar'>
<li class=""><a title="Go to dashboard" class="back-link" href="/gitlab/"><i class="fa fa-caret-square-o-left fa-fw"></i>
<span>
Go to dashboard
</span>
</a></li><li class='separate-item'></li>
<li class="home"><a title="Project" class="shortcuts-project" href="/gitlab/gellings/im2att_tf"><i class="fa fa-bookmark fa-fw"></i>
<span>
Project
</span>
</a></li><li class=""><a title="Activity" class="shortcuts-project-activity" href="/gitlab/gellings/im2att_tf/activity"><i class="fa fa-dashboard fa-fw"></i>
<span>
Activity
</span>
</a></li><li class="active"><a title="Files" class="shortcuts-tree" href="/gitlab/gellings/im2att_tf/tree/master"><i class="fa fa-files-o fa-fw"></i>
<span>
Files
</span>
</a></li><li class=""><a title="Commits" class="shortcuts-commits" href="/gitlab/gellings/im2att_tf/commits/master"><i class="fa fa-history fa-fw"></i>
<span>
Commits
</span>
</a></li><li class=""><a title="Graphs" class="shortcuts-graphs" href="/gitlab/gellings/im2att_tf/graphs/master"><i class="fa fa-area-chart fa-fw"></i>
<span>
Graphs
</span>
</a></li><li class=""><a title="Milestones" href="/gitlab/gellings/im2att_tf/milestones"><i class="fa fa-clock-o fa-fw"></i>
<span>
Milestones
</span>
</a></li><li class=""><a title="Issues" class="shortcuts-issues" href="/gitlab/gellings/im2att_tf/issues"><i class="fa fa-exclamation-circle fa-fw"></i>
<span>
Issues
<span class='count issue_counter'>0</span>
</span>
</a></li><li class=""><a title="Merge Requests" class="shortcuts-merge_requests" href="/gitlab/gellings/im2att_tf/merge_requests"><i class="fa fa-tasks fa-fw"></i>
<span>
Merge Requests
<span class='count merge_counter'>0</span>
</span>
</a></li><li class=""><a title="Members" class="team-tab tab" href="/gitlab/gellings/im2att_tf/project_members"><i class="fa fa-users fa-fw"></i>
<span>
Members
</span>
</a></li><li class=""><a title="Labels" href="/gitlab/gellings/im2att_tf/labels"><i class="fa fa-tags fa-fw"></i>
<span>
Labels
</span>
</a></li><li class=""><a title="Wiki" class="shortcuts-wiki" href="/gitlab/gellings/im2att_tf/wikis/home"><i class="fa fa-book fa-fw"></i>
<span>
Wiki
</span>
</a></li><li class=""><a title="Forks" href="/gitlab/gellings/im2att_tf/forks"><i class="fa fa-code-fork fa-fw"></i>
<span>
Forks
</span>
</a></li><li class="separate-item"><a title="Settings" href="/gitlab/gellings/im2att_tf/edit"><i class="fa fa-cogs fa-fw"></i>
<span>
Settings
</span>
</a></li><li class='hidden'>
<a title="Network" class="shortcuts-network" href="/gitlab/gellings/im2att_tf/network/master">Network
</a></li>
</ul>

<div class='collapse-nav'>
<a class="toggle-nav-collapse" title="Open/Close" href="#"><i class="fa fa-angle-right"></i></a>

</div>
<a class="sidebar-user" title="Profile" href="/gitlab/u/gellings"><img alt="Profile" class="avatar avatar s36" src="https://secure.gravatar.com/avatar/c60e455c80f0950bce953376b7ae15e8?s=120&amp;d=identicon" />
<div class='username'>
gellings
</div>
</a></div>
<div class='content-wrapper'>
<div class='flash-container'>
</div>


<div class='container-fluid container-limited'>
<div class='content'>
<div class='clearfix'>


<div class='tree-holder' id='tree-holder'>
<div class='nav-block'>
<div class='tree-ref-holder'>
<form class="project-refs-form" action="/gitlab/gellings/im2att_tf/refs/switch" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" />
<select name="ref" id="ref" class="project-refs-select select2 select2-sm"><optgroup label="Branches"><option value="levelswitch">levelswitch</option>
<option selected="selected" value="master">master</option>
<option value="rm_agment">rm_agment</option>
<option value="vo">vo</option></optgroup><optgroup label="Tags"></optgroup></select>
<input type="hidden" name="destination" id="destination" value="blob" />
<input type="hidden" name="path" id="path" value="vgg16.py" />
</form>


</div>
<ul class='breadcrumb repo-breadcrumb'>
<li>
<a href="/gitlab/gellings/im2att_tf/tree/master">im2att_tf
</a></li>
<li>
<a href="/gitlab/gellings/im2att_tf/blob/master/vgg16.py"><strong>
vgg16.py
</strong>
</a></li>
</ul>
</div>
<ul class='blob-commit-info hidden-xs'>
<li class='commit js-toggle-container' id='commit-8cccbde4'>
<div class='commit-row-title'>
<span class='item-title str-truncated'>
<a class="commit-row-message" href="/gitlab/gellings/im2att_tf/commit/8cccbde4c935c73a03d86c1dcaf5c52b6e974923">this is how I ended my 501R semester project</a>
</span>
<div class='pull-right'>
<button class="btn btn-clipboard" data-clipboard-text="8cccbde4c935c73a03d86c1dcaf5c52b6e974923" type="button"><i class="fa fa-clipboard"></i></button>
<a class="commit_short_id" href="/gitlab/gellings/im2att_tf/commit/8cccbde4c935c73a03d86c1dcaf5c52b6e974923">8cccbde4</a>
</div>
<div class='notes_count'>
</div>
</div>
<div class='commit-row-info'>
<a class="commit-author-link has_tooltip" title="gellings13@gmail.com" href="/gitlab/u/gellings"><img class="avatar s24" width="24" alt="" src="https://secure.gravatar.com/avatar/c60e455c80f0950bce953376b7ae15e8?s=48&amp;d=identicon" /> <span class="commit-author-name">Gary Ellingson</span></a>
authored
<div class='committed_ago'>
<time class="time_ago js-timeago " datetime="2016-12-21T23:04:32Z" title="Dec 21, 2016 11:04pm" data-toggle="tooltip" data-placement="top" data-container="body">2016-12-21 16:04:32 -0700</time> &nbsp;
</div>
<a class="pull-right" href="/gitlab/gellings/im2att_tf/tree/8cccbde4c935c73a03d86c1dcaf5c52b6e974923">Browse Files »</a>
</div>
</li>

</ul>
<div class='blob-content-holder' id='blob-content-holder'>
<article class='file-holder'>
<div class='file-title'>
<i class="fa fa-file-text-o fa-fw"></i>
<strong>
vgg16.py
</strong>
<small>
13.3 KB
</small>
<div class='file-actions hidden-xs'>
<div class='btn-group tree-btn-group'>
<a class="btn btn-sm" target="_blank" href="/gitlab/gellings/im2att_tf/raw/master/vgg16.py">Raw</a>
<a class="btn btn-sm" href="/gitlab/gellings/im2att_tf/blame/master/vgg16.py">Blame</a>
<a class="btn btn-sm" href="/gitlab/gellings/im2att_tf/commits/master/vgg16.py">History</a>
<a class="btn btn-sm" href="/gitlab/gellings/im2att_tf/blob/35800e34a884f7ab4ef9c6da37aeb31bf89ec15e/vgg16.py">Permalink</a>
</div>
<div class='btn-group' role='group'>
<a class="btn" href="/gitlab/gellings/im2att_tf/edit/master/vgg16.py">Edit</a>
<button name="button" type="submit" class="btn btn-default" data-target="#modal-upload-blob" data-toggle="modal">Replace</button>
<button name="button" type="submit" class="btn btn-remove" data-target="#modal-remove-blob" data-toggle="modal">Delete</button>
</div>

</div>
</div>
<div class='file-content code js-syntax-highlight'>
<div class='line-numbers'>
<a class='diff-line-num' data-line-number='1' href='#L1' id='L1'>
<i class='fa fa-link'></i>
1
</a>
<a class='diff-line-num' data-line-number='2' href='#L2' id='L2'>
<i class='fa fa-link'></i>
2
</a>
<a class='diff-line-num' data-line-number='3' href='#L3' id='L3'>
<i class='fa fa-link'></i>
3
</a>
<a class='diff-line-num' data-line-number='4' href='#L4' id='L4'>
<i class='fa fa-link'></i>
4
</a>
<a class='diff-line-num' data-line-number='5' href='#L5' id='L5'>
<i class='fa fa-link'></i>
5
</a>
<a class='diff-line-num' data-line-number='6' href='#L6' id='L6'>
<i class='fa fa-link'></i>
6
</a>
<a class='diff-line-num' data-line-number='7' href='#L7' id='L7'>
<i class='fa fa-link'></i>
7
</a>
<a class='diff-line-num' data-line-number='8' href='#L8' id='L8'>
<i class='fa fa-link'></i>
8
</a>
<a class='diff-line-num' data-line-number='9' href='#L9' id='L9'>
<i class='fa fa-link'></i>
9
</a>
<a class='diff-line-num' data-line-number='10' href='#L10' id='L10'>
<i class='fa fa-link'></i>
10
</a>
<a class='diff-line-num' data-line-number='11' href='#L11' id='L11'>
<i class='fa fa-link'></i>
11
</a>
<a class='diff-line-num' data-line-number='12' href='#L12' id='L12'>
<i class='fa fa-link'></i>
12
</a>
<a class='diff-line-num' data-line-number='13' href='#L13' id='L13'>
<i class='fa fa-link'></i>
13
</a>
<a class='diff-line-num' data-line-number='14' href='#L14' id='L14'>
<i class='fa fa-link'></i>
14
</a>
<a class='diff-line-num' data-line-number='15' href='#L15' id='L15'>
<i class='fa fa-link'></i>
15
</a>
<a class='diff-line-num' data-line-number='16' href='#L16' id='L16'>
<i class='fa fa-link'></i>
16
</a>
<a class='diff-line-num' data-line-number='17' href='#L17' id='L17'>
<i class='fa fa-link'></i>
17
</a>
<a class='diff-line-num' data-line-number='18' href='#L18' id='L18'>
<i class='fa fa-link'></i>
18
</a>
<a class='diff-line-num' data-line-number='19' href='#L19' id='L19'>
<i class='fa fa-link'></i>
19
</a>
<a class='diff-line-num' data-line-number='20' href='#L20' id='L20'>
<i class='fa fa-link'></i>
20
</a>
<a class='diff-line-num' data-line-number='21' href='#L21' id='L21'>
<i class='fa fa-link'></i>
21
</a>
<a class='diff-line-num' data-line-number='22' href='#L22' id='L22'>
<i class='fa fa-link'></i>
22
</a>
<a class='diff-line-num' data-line-number='23' href='#L23' id='L23'>
<i class='fa fa-link'></i>
23
</a>
<a class='diff-line-num' data-line-number='24' href='#L24' id='L24'>
<i class='fa fa-link'></i>
24
</a>
<a class='diff-line-num' data-line-number='25' href='#L25' id='L25'>
<i class='fa fa-link'></i>
25
</a>
<a class='diff-line-num' data-line-number='26' href='#L26' id='L26'>
<i class='fa fa-link'></i>
26
</a>
<a class='diff-line-num' data-line-number='27' href='#L27' id='L27'>
<i class='fa fa-link'></i>
27
</a>
<a class='diff-line-num' data-line-number='28' href='#L28' id='L28'>
<i class='fa fa-link'></i>
28
</a>
<a class='diff-line-num' data-line-number='29' href='#L29' id='L29'>
<i class='fa fa-link'></i>
29
</a>
<a class='diff-line-num' data-line-number='30' href='#L30' id='L30'>
<i class='fa fa-link'></i>
30
</a>
<a class='diff-line-num' data-line-number='31' href='#L31' id='L31'>
<i class='fa fa-link'></i>
31
</a>
<a class='diff-line-num' data-line-number='32' href='#L32' id='L32'>
<i class='fa fa-link'></i>
32
</a>
<a class='diff-line-num' data-line-number='33' href='#L33' id='L33'>
<i class='fa fa-link'></i>
33
</a>
<a class='diff-line-num' data-line-number='34' href='#L34' id='L34'>
<i class='fa fa-link'></i>
34
</a>
<a class='diff-line-num' data-line-number='35' href='#L35' id='L35'>
<i class='fa fa-link'></i>
35
</a>
<a class='diff-line-num' data-line-number='36' href='#L36' id='L36'>
<i class='fa fa-link'></i>
36
</a>
<a class='diff-line-num' data-line-number='37' href='#L37' id='L37'>
<i class='fa fa-link'></i>
37
</a>
<a class='diff-line-num' data-line-number='38' href='#L38' id='L38'>
<i class='fa fa-link'></i>
38
</a>
<a class='diff-line-num' data-line-number='39' href='#L39' id='L39'>
<i class='fa fa-link'></i>
39
</a>
<a class='diff-line-num' data-line-number='40' href='#L40' id='L40'>
<i class='fa fa-link'></i>
40
</a>
<a class='diff-line-num' data-line-number='41' href='#L41' id='L41'>
<i class='fa fa-link'></i>
41
</a>
<a class='diff-line-num' data-line-number='42' href='#L42' id='L42'>
<i class='fa fa-link'></i>
42
</a>
<a class='diff-line-num' data-line-number='43' href='#L43' id='L43'>
<i class='fa fa-link'></i>
43
</a>
<a class='diff-line-num' data-line-number='44' href='#L44' id='L44'>
<i class='fa fa-link'></i>
44
</a>
<a class='diff-line-num' data-line-number='45' href='#L45' id='L45'>
<i class='fa fa-link'></i>
45
</a>
<a class='diff-line-num' data-line-number='46' href='#L46' id='L46'>
<i class='fa fa-link'></i>
46
</a>
<a class='diff-line-num' data-line-number='47' href='#L47' id='L47'>
<i class='fa fa-link'></i>
47
</a>
<a class='diff-line-num' data-line-number='48' href='#L48' id='L48'>
<i class='fa fa-link'></i>
48
</a>
<a class='diff-line-num' data-line-number='49' href='#L49' id='L49'>
<i class='fa fa-link'></i>
49
</a>
<a class='diff-line-num' data-line-number='50' href='#L50' id='L50'>
<i class='fa fa-link'></i>
50
</a>
<a class='diff-line-num' data-line-number='51' href='#L51' id='L51'>
<i class='fa fa-link'></i>
51
</a>
<a class='diff-line-num' data-line-number='52' href='#L52' id='L52'>
<i class='fa fa-link'></i>
52
</a>
<a class='diff-line-num' data-line-number='53' href='#L53' id='L53'>
<i class='fa fa-link'></i>
53
</a>
<a class='diff-line-num' data-line-number='54' href='#L54' id='L54'>
<i class='fa fa-link'></i>
54
</a>
<a class='diff-line-num' data-line-number='55' href='#L55' id='L55'>
<i class='fa fa-link'></i>
55
</a>
<a class='diff-line-num' data-line-number='56' href='#L56' id='L56'>
<i class='fa fa-link'></i>
56
</a>
<a class='diff-line-num' data-line-number='57' href='#L57' id='L57'>
<i class='fa fa-link'></i>
57
</a>
<a class='diff-line-num' data-line-number='58' href='#L58' id='L58'>
<i class='fa fa-link'></i>
58
</a>
<a class='diff-line-num' data-line-number='59' href='#L59' id='L59'>
<i class='fa fa-link'></i>
59
</a>
<a class='diff-line-num' data-line-number='60' href='#L60' id='L60'>
<i class='fa fa-link'></i>
60
</a>
<a class='diff-line-num' data-line-number='61' href='#L61' id='L61'>
<i class='fa fa-link'></i>
61
</a>
<a class='diff-line-num' data-line-number='62' href='#L62' id='L62'>
<i class='fa fa-link'></i>
62
</a>
<a class='diff-line-num' data-line-number='63' href='#L63' id='L63'>
<i class='fa fa-link'></i>
63
</a>
<a class='diff-line-num' data-line-number='64' href='#L64' id='L64'>
<i class='fa fa-link'></i>
64
</a>
<a class='diff-line-num' data-line-number='65' href='#L65' id='L65'>
<i class='fa fa-link'></i>
65
</a>
<a class='diff-line-num' data-line-number='66' href='#L66' id='L66'>
<i class='fa fa-link'></i>
66
</a>
<a class='diff-line-num' data-line-number='67' href='#L67' id='L67'>
<i class='fa fa-link'></i>
67
</a>
<a class='diff-line-num' data-line-number='68' href='#L68' id='L68'>
<i class='fa fa-link'></i>
68
</a>
<a class='diff-line-num' data-line-number='69' href='#L69' id='L69'>
<i class='fa fa-link'></i>
69
</a>
<a class='diff-line-num' data-line-number='70' href='#L70' id='L70'>
<i class='fa fa-link'></i>
70
</a>
<a class='diff-line-num' data-line-number='71' href='#L71' id='L71'>
<i class='fa fa-link'></i>
71
</a>
<a class='diff-line-num' data-line-number='72' href='#L72' id='L72'>
<i class='fa fa-link'></i>
72
</a>
<a class='diff-line-num' data-line-number='73' href='#L73' id='L73'>
<i class='fa fa-link'></i>
73
</a>
<a class='diff-line-num' data-line-number='74' href='#L74' id='L74'>
<i class='fa fa-link'></i>
74
</a>
<a class='diff-line-num' data-line-number='75' href='#L75' id='L75'>
<i class='fa fa-link'></i>
75
</a>
<a class='diff-line-num' data-line-number='76' href='#L76' id='L76'>
<i class='fa fa-link'></i>
76
</a>
<a class='diff-line-num' data-line-number='77' href='#L77' id='L77'>
<i class='fa fa-link'></i>
77
</a>
<a class='diff-line-num' data-line-number='78' href='#L78' id='L78'>
<i class='fa fa-link'></i>
78
</a>
<a class='diff-line-num' data-line-number='79' href='#L79' id='L79'>
<i class='fa fa-link'></i>
79
</a>
<a class='diff-line-num' data-line-number='80' href='#L80' id='L80'>
<i class='fa fa-link'></i>
80
</a>
<a class='diff-line-num' data-line-number='81' href='#L81' id='L81'>
<i class='fa fa-link'></i>
81
</a>
<a class='diff-line-num' data-line-number='82' href='#L82' id='L82'>
<i class='fa fa-link'></i>
82
</a>
<a class='diff-line-num' data-line-number='83' href='#L83' id='L83'>
<i class='fa fa-link'></i>
83
</a>
<a class='diff-line-num' data-line-number='84' href='#L84' id='L84'>
<i class='fa fa-link'></i>
84
</a>
<a class='diff-line-num' data-line-number='85' href='#L85' id='L85'>
<i class='fa fa-link'></i>
85
</a>
<a class='diff-line-num' data-line-number='86' href='#L86' id='L86'>
<i class='fa fa-link'></i>
86
</a>
<a class='diff-line-num' data-line-number='87' href='#L87' id='L87'>
<i class='fa fa-link'></i>
87
</a>
<a class='diff-line-num' data-line-number='88' href='#L88' id='L88'>
<i class='fa fa-link'></i>
88
</a>
<a class='diff-line-num' data-line-number='89' href='#L89' id='L89'>
<i class='fa fa-link'></i>
89
</a>
<a class='diff-line-num' data-line-number='90' href='#L90' id='L90'>
<i class='fa fa-link'></i>
90
</a>
<a class='diff-line-num' data-line-number='91' href='#L91' id='L91'>
<i class='fa fa-link'></i>
91
</a>
<a class='diff-line-num' data-line-number='92' href='#L92' id='L92'>
<i class='fa fa-link'></i>
92
</a>
<a class='diff-line-num' data-line-number='93' href='#L93' id='L93'>
<i class='fa fa-link'></i>
93
</a>
<a class='diff-line-num' data-line-number='94' href='#L94' id='L94'>
<i class='fa fa-link'></i>
94
</a>
<a class='diff-line-num' data-line-number='95' href='#L95' id='L95'>
<i class='fa fa-link'></i>
95
</a>
<a class='diff-line-num' data-line-number='96' href='#L96' id='L96'>
<i class='fa fa-link'></i>
96
</a>
<a class='diff-line-num' data-line-number='97' href='#L97' id='L97'>
<i class='fa fa-link'></i>
97
</a>
<a class='diff-line-num' data-line-number='98' href='#L98' id='L98'>
<i class='fa fa-link'></i>
98
</a>
<a class='diff-line-num' data-line-number='99' href='#L99' id='L99'>
<i class='fa fa-link'></i>
99
</a>
<a class='diff-line-num' data-line-number='100' href='#L100' id='L100'>
<i class='fa fa-link'></i>
100
</a>
<a class='diff-line-num' data-line-number='101' href='#L101' id='L101'>
<i class='fa fa-link'></i>
101
</a>
<a class='diff-line-num' data-line-number='102' href='#L102' id='L102'>
<i class='fa fa-link'></i>
102
</a>
<a class='diff-line-num' data-line-number='103' href='#L103' id='L103'>
<i class='fa fa-link'></i>
103
</a>
<a class='diff-line-num' data-line-number='104' href='#L104' id='L104'>
<i class='fa fa-link'></i>
104
</a>
<a class='diff-line-num' data-line-number='105' href='#L105' id='L105'>
<i class='fa fa-link'></i>
105
</a>
<a class='diff-line-num' data-line-number='106' href='#L106' id='L106'>
<i class='fa fa-link'></i>
106
</a>
<a class='diff-line-num' data-line-number='107' href='#L107' id='L107'>
<i class='fa fa-link'></i>
107
</a>
<a class='diff-line-num' data-line-number='108' href='#L108' id='L108'>
<i class='fa fa-link'></i>
108
</a>
<a class='diff-line-num' data-line-number='109' href='#L109' id='L109'>
<i class='fa fa-link'></i>
109
</a>
<a class='diff-line-num' data-line-number='110' href='#L110' id='L110'>
<i class='fa fa-link'></i>
110
</a>
<a class='diff-line-num' data-line-number='111' href='#L111' id='L111'>
<i class='fa fa-link'></i>
111
</a>
<a class='diff-line-num' data-line-number='112' href='#L112' id='L112'>
<i class='fa fa-link'></i>
112
</a>
<a class='diff-line-num' data-line-number='113' href='#L113' id='L113'>
<i class='fa fa-link'></i>
113
</a>
<a class='diff-line-num' data-line-number='114' href='#L114' id='L114'>
<i class='fa fa-link'></i>
114
</a>
<a class='diff-line-num' data-line-number='115' href='#L115' id='L115'>
<i class='fa fa-link'></i>
115
</a>
<a class='diff-line-num' data-line-number='116' href='#L116' id='L116'>
<i class='fa fa-link'></i>
116
</a>
<a class='diff-line-num' data-line-number='117' href='#L117' id='L117'>
<i class='fa fa-link'></i>
117
</a>
<a class='diff-line-num' data-line-number='118' href='#L118' id='L118'>
<i class='fa fa-link'></i>
118
</a>
<a class='diff-line-num' data-line-number='119' href='#L119' id='L119'>
<i class='fa fa-link'></i>
119
</a>
<a class='diff-line-num' data-line-number='120' href='#L120' id='L120'>
<i class='fa fa-link'></i>
120
</a>
<a class='diff-line-num' data-line-number='121' href='#L121' id='L121'>
<i class='fa fa-link'></i>
121
</a>
<a class='diff-line-num' data-line-number='122' href='#L122' id='L122'>
<i class='fa fa-link'></i>
122
</a>
<a class='diff-line-num' data-line-number='123' href='#L123' id='L123'>
<i class='fa fa-link'></i>
123
</a>
<a class='diff-line-num' data-line-number='124' href='#L124' id='L124'>
<i class='fa fa-link'></i>
124
</a>
<a class='diff-line-num' data-line-number='125' href='#L125' id='L125'>
<i class='fa fa-link'></i>
125
</a>
<a class='diff-line-num' data-line-number='126' href='#L126' id='L126'>
<i class='fa fa-link'></i>
126
</a>
<a class='diff-line-num' data-line-number='127' href='#L127' id='L127'>
<i class='fa fa-link'></i>
127
</a>
<a class='diff-line-num' data-line-number='128' href='#L128' id='L128'>
<i class='fa fa-link'></i>
128
</a>
<a class='diff-line-num' data-line-number='129' href='#L129' id='L129'>
<i class='fa fa-link'></i>
129
</a>
<a class='diff-line-num' data-line-number='130' href='#L130' id='L130'>
<i class='fa fa-link'></i>
130
</a>
<a class='diff-line-num' data-line-number='131' href='#L131' id='L131'>
<i class='fa fa-link'></i>
131
</a>
<a class='diff-line-num' data-line-number='132' href='#L132' id='L132'>
<i class='fa fa-link'></i>
132
</a>
<a class='diff-line-num' data-line-number='133' href='#L133' id='L133'>
<i class='fa fa-link'></i>
133
</a>
<a class='diff-line-num' data-line-number='134' href='#L134' id='L134'>
<i class='fa fa-link'></i>
134
</a>
<a class='diff-line-num' data-line-number='135' href='#L135' id='L135'>
<i class='fa fa-link'></i>
135
</a>
<a class='diff-line-num' data-line-number='136' href='#L136' id='L136'>
<i class='fa fa-link'></i>
136
</a>
<a class='diff-line-num' data-line-number='137' href='#L137' id='L137'>
<i class='fa fa-link'></i>
137
</a>
<a class='diff-line-num' data-line-number='138' href='#L138' id='L138'>
<i class='fa fa-link'></i>
138
</a>
<a class='diff-line-num' data-line-number='139' href='#L139' id='L139'>
<i class='fa fa-link'></i>
139
</a>
<a class='diff-line-num' data-line-number='140' href='#L140' id='L140'>
<i class='fa fa-link'></i>
140
</a>
<a class='diff-line-num' data-line-number='141' href='#L141' id='L141'>
<i class='fa fa-link'></i>
141
</a>
<a class='diff-line-num' data-line-number='142' href='#L142' id='L142'>
<i class='fa fa-link'></i>
142
</a>
<a class='diff-line-num' data-line-number='143' href='#L143' id='L143'>
<i class='fa fa-link'></i>
143
</a>
<a class='diff-line-num' data-line-number='144' href='#L144' id='L144'>
<i class='fa fa-link'></i>
144
</a>
<a class='diff-line-num' data-line-number='145' href='#L145' id='L145'>
<i class='fa fa-link'></i>
145
</a>
<a class='diff-line-num' data-line-number='146' href='#L146' id='L146'>
<i class='fa fa-link'></i>
146
</a>
<a class='diff-line-num' data-line-number='147' href='#L147' id='L147'>
<i class='fa fa-link'></i>
147
</a>
<a class='diff-line-num' data-line-number='148' href='#L148' id='L148'>
<i class='fa fa-link'></i>
148
</a>
<a class='diff-line-num' data-line-number='149' href='#L149' id='L149'>
<i class='fa fa-link'></i>
149
</a>
<a class='diff-line-num' data-line-number='150' href='#L150' id='L150'>
<i class='fa fa-link'></i>
150
</a>
<a class='diff-line-num' data-line-number='151' href='#L151' id='L151'>
<i class='fa fa-link'></i>
151
</a>
<a class='diff-line-num' data-line-number='152' href='#L152' id='L152'>
<i class='fa fa-link'></i>
152
</a>
<a class='diff-line-num' data-line-number='153' href='#L153' id='L153'>
<i class='fa fa-link'></i>
153
</a>
<a class='diff-line-num' data-line-number='154' href='#L154' id='L154'>
<i class='fa fa-link'></i>
154
</a>
<a class='diff-line-num' data-line-number='155' href='#L155' id='L155'>
<i class='fa fa-link'></i>
155
</a>
<a class='diff-line-num' data-line-number='156' href='#L156' id='L156'>
<i class='fa fa-link'></i>
156
</a>
<a class='diff-line-num' data-line-number='157' href='#L157' id='L157'>
<i class='fa fa-link'></i>
157
</a>
<a class='diff-line-num' data-line-number='158' href='#L158' id='L158'>
<i class='fa fa-link'></i>
158
</a>
<a class='diff-line-num' data-line-number='159' href='#L159' id='L159'>
<i class='fa fa-link'></i>
159
</a>
<a class='diff-line-num' data-line-number='160' href='#L160' id='L160'>
<i class='fa fa-link'></i>
160
</a>
<a class='diff-line-num' data-line-number='161' href='#L161' id='L161'>
<i class='fa fa-link'></i>
161
</a>
<a class='diff-line-num' data-line-number='162' href='#L162' id='L162'>
<i class='fa fa-link'></i>
162
</a>
<a class='diff-line-num' data-line-number='163' href='#L163' id='L163'>
<i class='fa fa-link'></i>
163
</a>
<a class='diff-line-num' data-line-number='164' href='#L164' id='L164'>
<i class='fa fa-link'></i>
164
</a>
<a class='diff-line-num' data-line-number='165' href='#L165' id='L165'>
<i class='fa fa-link'></i>
165
</a>
<a class='diff-line-num' data-line-number='166' href='#L166' id='L166'>
<i class='fa fa-link'></i>
166
</a>
<a class='diff-line-num' data-line-number='167' href='#L167' id='L167'>
<i class='fa fa-link'></i>
167
</a>
<a class='diff-line-num' data-line-number='168' href='#L168' id='L168'>
<i class='fa fa-link'></i>
168
</a>
<a class='diff-line-num' data-line-number='169' href='#L169' id='L169'>
<i class='fa fa-link'></i>
169
</a>
<a class='diff-line-num' data-line-number='170' href='#L170' id='L170'>
<i class='fa fa-link'></i>
170
</a>
<a class='diff-line-num' data-line-number='171' href='#L171' id='L171'>
<i class='fa fa-link'></i>
171
</a>
<a class='diff-line-num' data-line-number='172' href='#L172' id='L172'>
<i class='fa fa-link'></i>
172
</a>
<a class='diff-line-num' data-line-number='173' href='#L173' id='L173'>
<i class='fa fa-link'></i>
173
</a>
<a class='diff-line-num' data-line-number='174' href='#L174' id='L174'>
<i class='fa fa-link'></i>
174
</a>
<a class='diff-line-num' data-line-number='175' href='#L175' id='L175'>
<i class='fa fa-link'></i>
175
</a>
<a class='diff-line-num' data-line-number='176' href='#L176' id='L176'>
<i class='fa fa-link'></i>
176
</a>
<a class='diff-line-num' data-line-number='177' href='#L177' id='L177'>
<i class='fa fa-link'></i>
177
</a>
<a class='diff-line-num' data-line-number='178' href='#L178' id='L178'>
<i class='fa fa-link'></i>
178
</a>
<a class='diff-line-num' data-line-number='179' href='#L179' id='L179'>
<i class='fa fa-link'></i>
179
</a>
<a class='diff-line-num' data-line-number='180' href='#L180' id='L180'>
<i class='fa fa-link'></i>
180
</a>
<a class='diff-line-num' data-line-number='181' href='#L181' id='L181'>
<i class='fa fa-link'></i>
181
</a>
<a class='diff-line-num' data-line-number='182' href='#L182' id='L182'>
<i class='fa fa-link'></i>
182
</a>
<a class='diff-line-num' data-line-number='183' href='#L183' id='L183'>
<i class='fa fa-link'></i>
183
</a>
<a class='diff-line-num' data-line-number='184' href='#L184' id='L184'>
<i class='fa fa-link'></i>
184
</a>
<a class='diff-line-num' data-line-number='185' href='#L185' id='L185'>
<i class='fa fa-link'></i>
185
</a>
<a class='diff-line-num' data-line-number='186' href='#L186' id='L186'>
<i class='fa fa-link'></i>
186
</a>
<a class='diff-line-num' data-line-number='187' href='#L187' id='L187'>
<i class='fa fa-link'></i>
187
</a>
<a class='diff-line-num' data-line-number='188' href='#L188' id='L188'>
<i class='fa fa-link'></i>
188
</a>
<a class='diff-line-num' data-line-number='189' href='#L189' id='L189'>
<i class='fa fa-link'></i>
189
</a>
<a class='diff-line-num' data-line-number='190' href='#L190' id='L190'>
<i class='fa fa-link'></i>
190
</a>
<a class='diff-line-num' data-line-number='191' href='#L191' id='L191'>
<i class='fa fa-link'></i>
191
</a>
<a class='diff-line-num' data-line-number='192' href='#L192' id='L192'>
<i class='fa fa-link'></i>
192
</a>
<a class='diff-line-num' data-line-number='193' href='#L193' id='L193'>
<i class='fa fa-link'></i>
193
</a>
<a class='diff-line-num' data-line-number='194' href='#L194' id='L194'>
<i class='fa fa-link'></i>
194
</a>
<a class='diff-line-num' data-line-number='195' href='#L195' id='L195'>
<i class='fa fa-link'></i>
195
</a>
<a class='diff-line-num' data-line-number='196' href='#L196' id='L196'>
<i class='fa fa-link'></i>
196
</a>
<a class='diff-line-num' data-line-number='197' href='#L197' id='L197'>
<i class='fa fa-link'></i>
197
</a>
<a class='diff-line-num' data-line-number='198' href='#L198' id='L198'>
<i class='fa fa-link'></i>
198
</a>
<a class='diff-line-num' data-line-number='199' href='#L199' id='L199'>
<i class='fa fa-link'></i>
199
</a>
<a class='diff-line-num' data-line-number='200' href='#L200' id='L200'>
<i class='fa fa-link'></i>
200
</a>
<a class='diff-line-num' data-line-number='201' href='#L201' id='L201'>
<i class='fa fa-link'></i>
201
</a>
<a class='diff-line-num' data-line-number='202' href='#L202' id='L202'>
<i class='fa fa-link'></i>
202
</a>
<a class='diff-line-num' data-line-number='203' href='#L203' id='L203'>
<i class='fa fa-link'></i>
203
</a>
<a class='diff-line-num' data-line-number='204' href='#L204' id='L204'>
<i class='fa fa-link'></i>
204
</a>
<a class='diff-line-num' data-line-number='205' href='#L205' id='L205'>
<i class='fa fa-link'></i>
205
</a>
<a class='diff-line-num' data-line-number='206' href='#L206' id='L206'>
<i class='fa fa-link'></i>
206
</a>
<a class='diff-line-num' data-line-number='207' href='#L207' id='L207'>
<i class='fa fa-link'></i>
207
</a>
<a class='diff-line-num' data-line-number='208' href='#L208' id='L208'>
<i class='fa fa-link'></i>
208
</a>
<a class='diff-line-num' data-line-number='209' href='#L209' id='L209'>
<i class='fa fa-link'></i>
209
</a>
<a class='diff-line-num' data-line-number='210' href='#L210' id='L210'>
<i class='fa fa-link'></i>
210
</a>
<a class='diff-line-num' data-line-number='211' href='#L211' id='L211'>
<i class='fa fa-link'></i>
211
</a>
<a class='diff-line-num' data-line-number='212' href='#L212' id='L212'>
<i class='fa fa-link'></i>
212
</a>
<a class='diff-line-num' data-line-number='213' href='#L213' id='L213'>
<i class='fa fa-link'></i>
213
</a>
<a class='diff-line-num' data-line-number='214' href='#L214' id='L214'>
<i class='fa fa-link'></i>
214
</a>
<a class='diff-line-num' data-line-number='215' href='#L215' id='L215'>
<i class='fa fa-link'></i>
215
</a>
<a class='diff-line-num' data-line-number='216' href='#L216' id='L216'>
<i class='fa fa-link'></i>
216
</a>
<a class='diff-line-num' data-line-number='217' href='#L217' id='L217'>
<i class='fa fa-link'></i>
217
</a>
<a class='diff-line-num' data-line-number='218' href='#L218' id='L218'>
<i class='fa fa-link'></i>
218
</a>
<a class='diff-line-num' data-line-number='219' href='#L219' id='L219'>
<i class='fa fa-link'></i>
219
</a>
<a class='diff-line-num' data-line-number='220' href='#L220' id='L220'>
<i class='fa fa-link'></i>
220
</a>
<a class='diff-line-num' data-line-number='221' href='#L221' id='L221'>
<i class='fa fa-link'></i>
221
</a>
<a class='diff-line-num' data-line-number='222' href='#L222' id='L222'>
<i class='fa fa-link'></i>
222
</a>
<a class='diff-line-num' data-line-number='223' href='#L223' id='L223'>
<i class='fa fa-link'></i>
223
</a>
<a class='diff-line-num' data-line-number='224' href='#L224' id='L224'>
<i class='fa fa-link'></i>
224
</a>
<a class='diff-line-num' data-line-number='225' href='#L225' id='L225'>
<i class='fa fa-link'></i>
225
</a>
<a class='diff-line-num' data-line-number='226' href='#L226' id='L226'>
<i class='fa fa-link'></i>
226
</a>
<a class='diff-line-num' data-line-number='227' href='#L227' id='L227'>
<i class='fa fa-link'></i>
227
</a>
<a class='diff-line-num' data-line-number='228' href='#L228' id='L228'>
<i class='fa fa-link'></i>
228
</a>
<a class='diff-line-num' data-line-number='229' href='#L229' id='L229'>
<i class='fa fa-link'></i>
229
</a>
<a class='diff-line-num' data-line-number='230' href='#L230' id='L230'>
<i class='fa fa-link'></i>
230
</a>
<a class='diff-line-num' data-line-number='231' href='#L231' id='L231'>
<i class='fa fa-link'></i>
231
</a>
<a class='diff-line-num' data-line-number='232' href='#L232' id='L232'>
<i class='fa fa-link'></i>
232
</a>
<a class='diff-line-num' data-line-number='233' href='#L233' id='L233'>
<i class='fa fa-link'></i>
233
</a>
<a class='diff-line-num' data-line-number='234' href='#L234' id='L234'>
<i class='fa fa-link'></i>
234
</a>
<a class='diff-line-num' data-line-number='235' href='#L235' id='L235'>
<i class='fa fa-link'></i>
235
</a>
<a class='diff-line-num' data-line-number='236' href='#L236' id='L236'>
<i class='fa fa-link'></i>
236
</a>
<a class='diff-line-num' data-line-number='237' href='#L237' id='L237'>
<i class='fa fa-link'></i>
237
</a>
<a class='diff-line-num' data-line-number='238' href='#L238' id='L238'>
<i class='fa fa-link'></i>
238
</a>
<a class='diff-line-num' data-line-number='239' href='#L239' id='L239'>
<i class='fa fa-link'></i>
239
</a>
<a class='diff-line-num' data-line-number='240' href='#L240' id='L240'>
<i class='fa fa-link'></i>
240
</a>
<a class='diff-line-num' data-line-number='241' href='#L241' id='L241'>
<i class='fa fa-link'></i>
241
</a>
<a class='diff-line-num' data-line-number='242' href='#L242' id='L242'>
<i class='fa fa-link'></i>
242
</a>
<a class='diff-line-num' data-line-number='243' href='#L243' id='L243'>
<i class='fa fa-link'></i>
243
</a>
<a class='diff-line-num' data-line-number='244' href='#L244' id='L244'>
<i class='fa fa-link'></i>
244
</a>
<a class='diff-line-num' data-line-number='245' href='#L245' id='L245'>
<i class='fa fa-link'></i>
245
</a>
<a class='diff-line-num' data-line-number='246' href='#L246' id='L246'>
<i class='fa fa-link'></i>
246
</a>
<a class='diff-line-num' data-line-number='247' href='#L247' id='L247'>
<i class='fa fa-link'></i>
247
</a>
<a class='diff-line-num' data-line-number='248' href='#L248' id='L248'>
<i class='fa fa-link'></i>
248
</a>
<a class='diff-line-num' data-line-number='249' href='#L249' id='L249'>
<i class='fa fa-link'></i>
249
</a>
<a class='diff-line-num' data-line-number='250' href='#L250' id='L250'>
<i class='fa fa-link'></i>
250
</a>
<a class='diff-line-num' data-line-number='251' href='#L251' id='L251'>
<i class='fa fa-link'></i>
251
</a>
<a class='diff-line-num' data-line-number='252' href='#L252' id='L252'>
<i class='fa fa-link'></i>
252
</a>
<a class='diff-line-num' data-line-number='253' href='#L253' id='L253'>
<i class='fa fa-link'></i>
253
</a>
<a class='diff-line-num' data-line-number='254' href='#L254' id='L254'>
<i class='fa fa-link'></i>
254
</a>
<a class='diff-line-num' data-line-number='255' href='#L255' id='L255'>
<i class='fa fa-link'></i>
255
</a>
<a class='diff-line-num' data-line-number='256' href='#L256' id='L256'>
<i class='fa fa-link'></i>
256
</a>
<a class='diff-line-num' data-line-number='257' href='#L257' id='L257'>
<i class='fa fa-link'></i>
257
</a>
<a class='diff-line-num' data-line-number='258' href='#L258' id='L258'>
<i class='fa fa-link'></i>
258
</a>
<a class='diff-line-num' data-line-number='259' href='#L259' id='L259'>
<i class='fa fa-link'></i>
259
</a>
<a class='diff-line-num' data-line-number='260' href='#L260' id='L260'>
<i class='fa fa-link'></i>
260
</a>
<a class='diff-line-num' data-line-number='261' href='#L261' id='L261'>
<i class='fa fa-link'></i>
261
</a>
<a class='diff-line-num' data-line-number='262' href='#L262' id='L262'>
<i class='fa fa-link'></i>
262
</a>
<a class='diff-line-num' data-line-number='263' href='#L263' id='L263'>
<i class='fa fa-link'></i>
263
</a>
<a class='diff-line-num' data-line-number='264' href='#L264' id='L264'>
<i class='fa fa-link'></i>
264
</a>
<a class='diff-line-num' data-line-number='265' href='#L265' id='L265'>
<i class='fa fa-link'></i>
265
</a>
<a class='diff-line-num' data-line-number='266' href='#L266' id='L266'>
<i class='fa fa-link'></i>
266
</a>
<a class='diff-line-num' data-line-number='267' href='#L267' id='L267'>
<i class='fa fa-link'></i>
267
</a>
<a class='diff-line-num' data-line-number='268' href='#L268' id='L268'>
<i class='fa fa-link'></i>
268
</a>
<a class='diff-line-num' data-line-number='269' href='#L269' id='L269'>
<i class='fa fa-link'></i>
269
</a>
<a class='diff-line-num' data-line-number='270' href='#L270' id='L270'>
<i class='fa fa-link'></i>
270
</a>
<a class='diff-line-num' data-line-number='271' href='#L271' id='L271'>
<i class='fa fa-link'></i>
271
</a>
<a class='diff-line-num' data-line-number='272' href='#L272' id='L272'>
<i class='fa fa-link'></i>
272
</a>
</div>
<div class='blob-content' data-blob-id='abbfda917ab378e2bed76818313e5471a0da9c6b'>
<pre class="code highlight"><code><span id="LC1" class="line"><span class="c">########################################################################################</span></span>
<span id="LC2" class="line"><span class="c"># Davi Frossard, 2016                                                                  #</span></span>
<span id="LC3" class="line"><span class="c"># VGG16 implementation in TensorFlow                                                   #</span></span>
<span id="LC4" class="line"><span class="c"># Details:                                                                             #</span></span>
<span id="LC5" class="line"><span class="c"># http://www.cs.toronto.edu/~frossard/post/vgg16/                                      #</span></span>
<span id="LC6" class="line"><span class="c">#                                                                                      #</span></span>
<span id="LC7" class="line"><span class="c"># Model from https://gist.github.com/ksimonyan/211839e770f7b538e2d8#file-readme-md     #</span></span>
<span id="LC8" class="line"><span class="c"># Weights from Caffe converted using https://github.com/ethereon/caffe-tensorflow      #</span></span>
<span id="LC9" class="line"><span class="c">########################################################################################</span></span>
<span id="LC10" class="line"></span>
<span id="LC11" class="line"><span class="c"># XXX a few simplifications by wingated</span></span>
<span id="LC12" class="line"></span>
<span id="LC13" class="line"><span class="kn">import</span> <span class="nn">tensorflow</span> <span class="kn">as</span> <span class="nn">tf</span></span>
<span id="LC14" class="line"><span class="kn">import</span> <span class="nn">numpy</span> <span class="kn">as</span> <span class="nn">np</span></span>
<span id="LC15" class="line"><span class="c">#from scipy.misc import imread, imresize</span></span>
<span id="LC16" class="line"><span class="c">#from imagenet_classes import class_names # XXX wingated</span></span>
<span id="LC17" class="line"></span>
<span id="LC18" class="line"><span class="k">class</span> <span class="nc">vgg16</span><span class="p">:</span></span>
<span id="LC19" class="line">    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">imgs</span><span class="p">,</span> <span class="n">weights</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">sess</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span>
<span id="LC20" class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">imgs</span> <span class="o">=</span> <span class="n">imgs</span></span>
<span id="LC21" class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">convlayers</span><span class="p">()</span></span>
<span id="LC22" class="line">        <span class="c"># XXX wingated</span></span>
<span id="LC23" class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">fc_layers</span><span class="p">()</span></span>
<span id="LC24" class="line"><span class="c">#        self.probs = tf.nn.softmax(self.fc3l)</span></span>
<span id="LC25" class="line">        <span class="k">if</span> <span class="n">weights</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span> <span class="ow">and</span> <span class="n">sess</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span></span>
<span id="LC26" class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">load_weights</span><span class="p">(</span><span class="n">weights</span><span class="p">,</span> <span class="n">sess</span><span class="p">)</span></span>
<span id="LC27" class="line"></span>
<span id="LC28" class="line"></span>
<span id="LC29" class="line">    <span class="k">def</span> <span class="nf">convlayers</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span>
<span id="LC30" class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">parameters</span> <span class="o">=</span> <span class="p">[]</span></span>
<span id="LC31" class="line"></span>
<span id="LC32" class="line">        <span class="c"># zero-mean input</span></span>
<span id="LC33" class="line">        <span class="k">with</span> <span class="n">tf</span><span class="o">.</span><span class="n">name_scope</span><span class="p">(</span><span class="s">&#39;preprocess&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">scope</span><span class="p">:</span></span>
<span id="LC34" class="line">            <span class="n">mean</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">constant</span><span class="p">([</span><span class="mf">123.68</span><span class="p">,</span> <span class="mf">116.779</span><span class="p">,</span> <span class="mf">103.939</span><span class="p">],</span> <span class="n">dtype</span><span class="o">=</span><span class="n">tf</span><span class="o">.</span><span class="n">float32</span><span class="p">,</span> <span class="n">shape</span><span class="o">=</span><span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">3</span><span class="p">],</span> <span class="n">name</span><span class="o">=</span><span class="s">&#39;img_mean&#39;</span><span class="p">)</span></span>
<span id="LC35" class="line">            <span class="n">images</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">imgs</span><span class="o">-</span><span class="n">mean</span></span>
<span id="LC36" class="line"></span>
<span id="LC37" class="line">        <span class="c"># conv1_1</span></span>
<span id="LC38" class="line">        <span class="k">with</span> <span class="n">tf</span><span class="o">.</span><span class="n">name_scope</span><span class="p">(</span><span class="s">&#39;conv1_1&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">scope</span><span class="p">:</span></span>
<span id="LC39" class="line">            <span class="n">kernel</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">Variable</span><span class="p">(</span><span class="n">tf</span><span class="o">.</span><span class="n">truncated_normal</span><span class="p">([</span><span class="mi">3</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">64</span><span class="p">],</span> <span class="n">dtype</span><span class="o">=</span><span class="n">tf</span><span class="o">.</span><span class="n">float32</span><span class="p">,</span></span>
<span id="LC40" class="line">                                                     <span class="n">stddev</span><span class="o">=</span><span class="mf">1e-1</span><span class="p">),</span> <span class="n">name</span><span class="o">=</span><span class="s">&#39;weights&#39;</span><span class="p">)</span></span>
<span id="LC41" class="line">            <span class="n">conv</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">nn</span><span class="o">.</span><span class="n">conv2d</span><span class="p">(</span><span class="n">images</span><span class="p">,</span> <span class="n">kernel</span><span class="p">,</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">],</span> <span class="n">padding</span><span class="o">=</span><span class="s">&#39;SAME&#39;</span><span class="p">)</span></span>
<span id="LC42" class="line">            <span class="n">biases</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">Variable</span><span class="p">(</span><span class="n">tf</span><span class="o">.</span><span class="n">constant</span><span class="p">(</span><span class="mf">0.0</span><span class="p">,</span> <span class="n">shape</span><span class="o">=</span><span class="p">[</span><span class="mi">64</span><span class="p">],</span> <span class="n">dtype</span><span class="o">=</span><span class="n">tf</span><span class="o">.</span><span class="n">float32</span><span class="p">),</span></span>
<span id="LC43" class="line">                                 <span class="n">trainable</span><span class="o">=</span><span class="bp">True</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="s">&#39;biases&#39;</span><span class="p">)</span></span>
<span id="LC44" class="line">            <span class="n">out</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">nn</span><span class="o">.</span><span class="n">bias_add</span><span class="p">(</span><span class="n">conv</span><span class="p">,</span> <span class="n">biases</span><span class="p">)</span></span>
<span id="LC45" class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">conv1_1</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">nn</span><span class="o">.</span><span class="n">relu</span><span class="p">(</span><span class="n">out</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="n">scope</span><span class="p">)</span></span>
<span id="LC46" class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">parameters</span> <span class="o">+=</span> <span class="p">[</span><span class="n">kernel</span><span class="p">,</span> <span class="n">biases</span><span class="p">]</span></span>
<span id="LC47" class="line"></span>
<span id="LC48" class="line">        <span class="c"># conv1_2</span></span>
<span id="LC49" class="line">        <span class="k">with</span> <span class="n">tf</span><span class="o">.</span><span class="n">name_scope</span><span class="p">(</span><span class="s">&#39;conv1_2&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">scope</span><span class="p">:</span></span>
<span id="LC50" class="line">            <span class="n">kernel</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">Variable</span><span class="p">(</span><span class="n">tf</span><span class="o">.</span><span class="n">truncated_normal</span><span class="p">([</span><span class="mi">3</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">64</span><span class="p">,</span> <span class="mi">64</span><span class="p">],</span> <span class="n">dtype</span><span class="o">=</span><span class="n">tf</span><span class="o">.</span><span class="n">float32</span><span class="p">,</span></span>
<span id="LC51" class="line">                                                     <span class="n">stddev</span><span class="o">=</span><span class="mf">1e-1</span><span class="p">),</span> <span class="n">name</span><span class="o">=</span><span class="s">&#39;weights&#39;</span><span class="p">)</span></span>
<span id="LC52" class="line">            <span class="n">conv</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">nn</span><span class="o">.</span><span class="n">conv2d</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">conv1_1</span><span class="p">,</span> <span class="n">kernel</span><span class="p">,</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">],</span> <span class="n">padding</span><span class="o">=</span><span class="s">&#39;SAME&#39;</span><span class="p">)</span></span>
<span id="LC53" class="line">            <span class="n">biases</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">Variable</span><span class="p">(</span><span class="n">tf</span><span class="o">.</span><span class="n">constant</span><span class="p">(</span><span class="mf">0.0</span><span class="p">,</span> <span class="n">shape</span><span class="o">=</span><span class="p">[</span><span class="mi">64</span><span class="p">],</span> <span class="n">dtype</span><span class="o">=</span><span class="n">tf</span><span class="o">.</span><span class="n">float32</span><span class="p">),</span></span>
<span id="LC54" class="line">                                 <span class="n">trainable</span><span class="o">=</span><span class="bp">True</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="s">&#39;biases&#39;</span><span class="p">)</span></span>
<span id="LC55" class="line">            <span class="n">out</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">nn</span><span class="o">.</span><span class="n">bias_add</span><span class="p">(</span><span class="n">conv</span><span class="p">,</span> <span class="n">biases</span><span class="p">)</span></span>
<span id="LC56" class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">conv1_2</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">nn</span><span class="o">.</span><span class="n">relu</span><span class="p">(</span><span class="n">out</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="n">scope</span><span class="p">)</span></span>
<span id="LC57" class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">parameters</span> <span class="o">+=</span> <span class="p">[</span><span class="n">kernel</span><span class="p">,</span> <span class="n">biases</span><span class="p">]</span></span>
<span id="LC58" class="line"></span>
<span id="LC59" class="line">        <span class="c"># pool1</span></span>
<span id="LC60" class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">pool1</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">nn</span><span class="o">.</span><span class="n">max_pool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">conv1_2</span><span class="p">,</span></span>
<span id="LC61" class="line">                               <span class="n">ksize</span><span class="o">=</span><span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">1</span><span class="p">],</span></span>
<span id="LC62" class="line">                               <span class="n">strides</span><span class="o">=</span><span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">1</span><span class="p">],</span></span>
<span id="LC63" class="line">                               <span class="n">padding</span><span class="o">=</span><span class="s">&#39;SAME&#39;</span><span class="p">,</span></span>
<span id="LC64" class="line">                               <span class="n">name</span><span class="o">=</span><span class="s">&#39;pool1&#39;</span><span class="p">)</span></span>
<span id="LC65" class="line"></span>
<span id="LC66" class="line">        <span class="c"># conv2_1</span></span>
<span id="LC67" class="line">        <span class="k">with</span> <span class="n">tf</span><span class="o">.</span><span class="n">name_scope</span><span class="p">(</span><span class="s">&#39;conv2_1&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">scope</span><span class="p">:</span></span>
<span id="LC68" class="line">            <span class="n">kernel</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">Variable</span><span class="p">(</span><span class="n">tf</span><span class="o">.</span><span class="n">truncated_normal</span><span class="p">([</span><span class="mi">3</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">64</span><span class="p">,</span> <span class="mi">128</span><span class="p">],</span> <span class="n">dtype</span><span class="o">=</span><span class="n">tf</span><span class="o">.</span><span class="n">float32</span><span class="p">,</span></span>
<span id="LC69" class="line">                                                     <span class="n">stddev</span><span class="o">=</span><span class="mf">1e-1</span><span class="p">),</span> <span class="n">name</span><span class="o">=</span><span class="s">&#39;weights&#39;</span><span class="p">)</span></span>
<span id="LC70" class="line">            <span class="n">conv</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">nn</span><span class="o">.</span><span class="n">conv2d</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">pool1</span><span class="p">,</span> <span class="n">kernel</span><span class="p">,</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">],</span> <span class="n">padding</span><span class="o">=</span><span class="s">&#39;SAME&#39;</span><span class="p">)</span></span>
<span id="LC71" class="line">            <span class="n">biases</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">Variable</span><span class="p">(</span><span class="n">tf</span><span class="o">.</span><span class="n">constant</span><span class="p">(</span><span class="mf">0.0</span><span class="p">,</span> <span class="n">shape</span><span class="o">=</span><span class="p">[</span><span class="mi">128</span><span class="p">],</span> <span class="n">dtype</span><span class="o">=</span><span class="n">tf</span><span class="o">.</span><span class="n">float32</span><span class="p">),</span></span>
<span id="LC72" class="line">                                 <span class="n">trainable</span><span class="o">=</span><span class="bp">True</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="s">&#39;biases&#39;</span><span class="p">)</span></span>
<span id="LC73" class="line">            <span class="n">out</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">nn</span><span class="o">.</span><span class="n">bias_add</span><span class="p">(</span><span class="n">conv</span><span class="p">,</span> <span class="n">biases</span><span class="p">)</span></span>
<span id="LC74" class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">conv2_1</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">nn</span><span class="o">.</span><span class="n">relu</span><span class="p">(</span><span class="n">out</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="n">scope</span><span class="p">)</span></span>
<span id="LC75" class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">parameters</span> <span class="o">+=</span> <span class="p">[</span><span class="n">kernel</span><span class="p">,</span> <span class="n">biases</span><span class="p">]</span></span>
<span id="LC76" class="line"></span>
<span id="LC77" class="line">        <span class="c"># conv2_2</span></span>
<span id="LC78" class="line">        <span class="k">with</span> <span class="n">tf</span><span class="o">.</span><span class="n">name_scope</span><span class="p">(</span><span class="s">&#39;conv2_2&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">scope</span><span class="p">:</span></span>
<span id="LC79" class="line">            <span class="n">kernel</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">Variable</span><span class="p">(</span><span class="n">tf</span><span class="o">.</span><span class="n">truncated_normal</span><span class="p">([</span><span class="mi">3</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">128</span><span class="p">,</span> <span class="mi">128</span><span class="p">],</span> <span class="n">dtype</span><span class="o">=</span><span class="n">tf</span><span class="o">.</span><span class="n">float32</span><span class="p">,</span></span>
<span id="LC80" class="line">                                                     <span class="n">stddev</span><span class="o">=</span><span class="mf">1e-1</span><span class="p">),</span> <span class="n">name</span><span class="o">=</span><span class="s">&#39;weights&#39;</span><span class="p">)</span></span>
<span id="LC81" class="line">            <span class="n">conv</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">nn</span><span class="o">.</span><span class="n">conv2d</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">conv2_1</span><span class="p">,</span> <span class="n">kernel</span><span class="p">,</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">],</span> <span class="n">padding</span><span class="o">=</span><span class="s">&#39;SAME&#39;</span><span class="p">)</span></span>
<span id="LC82" class="line">            <span class="n">biases</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">Variable</span><span class="p">(</span><span class="n">tf</span><span class="o">.</span><span class="n">constant</span><span class="p">(</span><span class="mf">0.0</span><span class="p">,</span> <span class="n">shape</span><span class="o">=</span><span class="p">[</span><span class="mi">128</span><span class="p">],</span> <span class="n">dtype</span><span class="o">=</span><span class="n">tf</span><span class="o">.</span><span class="n">float32</span><span class="p">),</span></span>
<span id="LC83" class="line">                                 <span class="n">trainable</span><span class="o">=</span><span class="bp">True</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="s">&#39;biases&#39;</span><span class="p">)</span></span>
<span id="LC84" class="line">            <span class="n">out</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">nn</span><span class="o">.</span><span class="n">bias_add</span><span class="p">(</span><span class="n">conv</span><span class="p">,</span> <span class="n">biases</span><span class="p">)</span></span>
<span id="LC85" class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">conv2_2</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">nn</span><span class="o">.</span><span class="n">relu</span><span class="p">(</span><span class="n">out</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="n">scope</span><span class="p">)</span></span>
<span id="LC86" class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">parameters</span> <span class="o">+=</span> <span class="p">[</span><span class="n">kernel</span><span class="p">,</span> <span class="n">biases</span><span class="p">]</span></span>
<span id="LC87" class="line"></span>
<span id="LC88" class="line">        <span class="c"># pool2</span></span>
<span id="LC89" class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">pool2</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">nn</span><span class="o">.</span><span class="n">max_pool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">conv2_2</span><span class="p">,</span></span>
<span id="LC90" class="line">                               <span class="n">ksize</span><span class="o">=</span><span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">1</span><span class="p">],</span></span>
<span id="LC91" class="line">                               <span class="n">strides</span><span class="o">=</span><span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">1</span><span class="p">],</span></span>
<span id="LC92" class="line">                               <span class="n">padding</span><span class="o">=</span><span class="s">&#39;SAME&#39;</span><span class="p">,</span></span>
<span id="LC93" class="line">                               <span class="n">name</span><span class="o">=</span><span class="s">&#39;pool2&#39;</span><span class="p">)</span></span>
<span id="LC94" class="line"></span>
<span id="LC95" class="line">        <span class="c"># conv3_1</span></span>
<span id="LC96" class="line">        <span class="k">with</span> <span class="n">tf</span><span class="o">.</span><span class="n">name_scope</span><span class="p">(</span><span class="s">&#39;conv3_1&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">scope</span><span class="p">:</span></span>
<span id="LC97" class="line">            <span class="n">kernel</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">Variable</span><span class="p">(</span><span class="n">tf</span><span class="o">.</span><span class="n">truncated_normal</span><span class="p">([</span><span class="mi">3</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">128</span><span class="p">,</span> <span class="mi">256</span><span class="p">],</span> <span class="n">dtype</span><span class="o">=</span><span class="n">tf</span><span class="o">.</span><span class="n">float32</span><span class="p">,</span></span>
<span id="LC98" class="line">                                                     <span class="n">stddev</span><span class="o">=</span><span class="mf">1e-1</span><span class="p">),</span> <span class="n">name</span><span class="o">=</span><span class="s">&#39;weights&#39;</span><span class="p">)</span></span>
<span id="LC99" class="line">            <span class="n">conv</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">nn</span><span class="o">.</span><span class="n">conv2d</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">pool2</span><span class="p">,</span> <span class="n">kernel</span><span class="p">,</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">],</span> <span class="n">padding</span><span class="o">=</span><span class="s">&#39;SAME&#39;</span><span class="p">)</span></span>
<span id="LC100" class="line">            <span class="n">biases</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">Variable</span><span class="p">(</span><span class="n">tf</span><span class="o">.</span><span class="n">constant</span><span class="p">(</span><span class="mf">0.0</span><span class="p">,</span> <span class="n">shape</span><span class="o">=</span><span class="p">[</span><span class="mi">256</span><span class="p">],</span> <span class="n">dtype</span><span class="o">=</span><span class="n">tf</span><span class="o">.</span><span class="n">float32</span><span class="p">),</span></span>
<span id="LC101" class="line">                                 <span class="n">trainable</span><span class="o">=</span><span class="bp">True</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="s">&#39;biases&#39;</span><span class="p">)</span></span>
<span id="LC102" class="line">            <span class="n">out</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">nn</span><span class="o">.</span><span class="n">bias_add</span><span class="p">(</span><span class="n">conv</span><span class="p">,</span> <span class="n">biases</span><span class="p">)</span></span>
<span id="LC103" class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">conv3_1</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">nn</span><span class="o">.</span><span class="n">relu</span><span class="p">(</span><span class="n">out</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="n">scope</span><span class="p">)</span></span>
<span id="LC104" class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">parameters</span> <span class="o">+=</span> <span class="p">[</span><span class="n">kernel</span><span class="p">,</span> <span class="n">biases</span><span class="p">]</span></span>
<span id="LC105" class="line"></span>
<span id="LC106" class="line">        <span class="c"># conv3_2</span></span>
<span id="LC107" class="line">        <span class="k">with</span> <span class="n">tf</span><span class="o">.</span><span class="n">name_scope</span><span class="p">(</span><span class="s">&#39;conv3_2&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">scope</span><span class="p">:</span></span>
<span id="LC108" class="line">            <span class="n">kernel</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">Variable</span><span class="p">(</span><span class="n">tf</span><span class="o">.</span><span class="n">truncated_normal</span><span class="p">([</span><span class="mi">3</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">256</span><span class="p">,</span> <span class="mi">256</span><span class="p">],</span> <span class="n">dtype</span><span class="o">=</span><span class="n">tf</span><span class="o">.</span><span class="n">float32</span><span class="p">,</span></span>
<span id="LC109" class="line">                                                     <span class="n">stddev</span><span class="o">=</span><span class="mf">1e-1</span><span class="p">),</span> <span class="n">name</span><span class="o">=</span><span class="s">&#39;weights&#39;</span><span class="p">)</span></span>
<span id="LC110" class="line">            <span class="n">conv</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">nn</span><span class="o">.</span><span class="n">conv2d</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">conv3_1</span><span class="p">,</span> <span class="n">kernel</span><span class="p">,</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">],</span> <span class="n">padding</span><span class="o">=</span><span class="s">&#39;SAME&#39;</span><span class="p">)</span></span>
<span id="LC111" class="line">            <span class="n">biases</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">Variable</span><span class="p">(</span><span class="n">tf</span><span class="o">.</span><span class="n">constant</span><span class="p">(</span><span class="mf">0.0</span><span class="p">,</span> <span class="n">shape</span><span class="o">=</span><span class="p">[</span><span class="mi">256</span><span class="p">],</span> <span class="n">dtype</span><span class="o">=</span><span class="n">tf</span><span class="o">.</span><span class="n">float32</span><span class="p">),</span></span>
<span id="LC112" class="line">                                 <span class="n">trainable</span><span class="o">=</span><span class="bp">True</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="s">&#39;biases&#39;</span><span class="p">)</span></span>
<span id="LC113" class="line">            <span class="n">out</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">nn</span><span class="o">.</span><span class="n">bias_add</span><span class="p">(</span><span class="n">conv</span><span class="p">,</span> <span class="n">biases</span><span class="p">)</span></span>
<span id="LC114" class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">conv3_2</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">nn</span><span class="o">.</span><span class="n">relu</span><span class="p">(</span><span class="n">out</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="n">scope</span><span class="p">)</span></span>
<span id="LC115" class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">parameters</span> <span class="o">+=</span> <span class="p">[</span><span class="n">kernel</span><span class="p">,</span> <span class="n">biases</span><span class="p">]</span></span>
<span id="LC116" class="line"></span>
<span id="LC117" class="line">        <span class="c"># conv3_3</span></span>
<span id="LC118" class="line">        <span class="k">with</span> <span class="n">tf</span><span class="o">.</span><span class="n">name_scope</span><span class="p">(</span><span class="s">&#39;conv3_3&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">scope</span><span class="p">:</span></span>
<span id="LC119" class="line">            <span class="n">kernel</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">Variable</span><span class="p">(</span><span class="n">tf</span><span class="o">.</span><span class="n">truncated_normal</span><span class="p">([</span><span class="mi">3</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">256</span><span class="p">,</span> <span class="mi">256</span><span class="p">],</span> <span class="n">dtype</span><span class="o">=</span><span class="n">tf</span><span class="o">.</span><span class="n">float32</span><span class="p">,</span></span>
<span id="LC120" class="line">                                                     <span class="n">stddev</span><span class="o">=</span><span class="mf">1e-1</span><span class="p">),</span> <span class="n">name</span><span class="o">=</span><span class="s">&#39;weights&#39;</span><span class="p">)</span></span>
<span id="LC121" class="line">            <span class="n">conv</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">nn</span><span class="o">.</span><span class="n">conv2d</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">conv3_2</span><span class="p">,</span> <span class="n">kernel</span><span class="p">,</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">],</span> <span class="n">padding</span><span class="o">=</span><span class="s">&#39;SAME&#39;</span><span class="p">)</span></span>
<span id="LC122" class="line">            <span class="n">biases</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">Variable</span><span class="p">(</span><span class="n">tf</span><span class="o">.</span><span class="n">constant</span><span class="p">(</span><span class="mf">0.0</span><span class="p">,</span> <span class="n">shape</span><span class="o">=</span><span class="p">[</span><span class="mi">256</span><span class="p">],</span> <span class="n">dtype</span><span class="o">=</span><span class="n">tf</span><span class="o">.</span><span class="n">float32</span><span class="p">),</span></span>
<span id="LC123" class="line">                                 <span class="n">trainable</span><span class="o">=</span><span class="bp">True</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="s">&#39;biases&#39;</span><span class="p">)</span></span>
<span id="LC124" class="line">            <span class="n">out</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">nn</span><span class="o">.</span><span class="n">bias_add</span><span class="p">(</span><span class="n">conv</span><span class="p">,</span> <span class="n">biases</span><span class="p">)</span></span>
<span id="LC125" class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">conv3_3</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">nn</span><span class="o">.</span><span class="n">relu</span><span class="p">(</span><span class="n">out</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="n">scope</span><span class="p">)</span></span>
<span id="LC126" class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">parameters</span> <span class="o">+=</span> <span class="p">[</span><span class="n">kernel</span><span class="p">,</span> <span class="n">biases</span><span class="p">]</span></span>
<span id="LC127" class="line"></span>
<span id="LC128" class="line">        <span class="c"># pool3</span></span>
<span id="LC129" class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">pool3</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">nn</span><span class="o">.</span><span class="n">max_pool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">conv3_3</span><span class="p">,</span></span>
<span id="LC130" class="line">                               <span class="n">ksize</span><span class="o">=</span><span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">1</span><span class="p">],</span></span>
<span id="LC131" class="line">                               <span class="n">strides</span><span class="o">=</span><span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">1</span><span class="p">],</span></span>
<span id="LC132" class="line">                               <span class="n">padding</span><span class="o">=</span><span class="s">&#39;SAME&#39;</span><span class="p">,</span></span>
<span id="LC133" class="line">                               <span class="n">name</span><span class="o">=</span><span class="s">&#39;pool3&#39;</span><span class="p">)</span></span>
<span id="LC134" class="line"></span>
<span id="LC135" class="line">        <span class="c"># conv4_1</span></span>
<span id="LC136" class="line">        <span class="k">with</span> <span class="n">tf</span><span class="o">.</span><span class="n">name_scope</span><span class="p">(</span><span class="s">&#39;conv4_1&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">scope</span><span class="p">:</span></span>
<span id="LC137" class="line">            <span class="n">kernel</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">Variable</span><span class="p">(</span><span class="n">tf</span><span class="o">.</span><span class="n">truncated_normal</span><span class="p">([</span><span class="mi">3</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">256</span><span class="p">,</span> <span class="mi">512</span><span class="p">],</span> <span class="n">dtype</span><span class="o">=</span><span class="n">tf</span><span class="o">.</span><span class="n">float32</span><span class="p">,</span></span>
<span id="LC138" class="line">                                                     <span class="n">stddev</span><span class="o">=</span><span class="mf">1e-1</span><span class="p">),</span> <span class="n">name</span><span class="o">=</span><span class="s">&#39;weights&#39;</span><span class="p">)</span></span>
<span id="LC139" class="line">            <span class="n">conv</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">nn</span><span class="o">.</span><span class="n">conv2d</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">pool3</span><span class="p">,</span> <span class="n">kernel</span><span class="p">,</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">],</span> <span class="n">padding</span><span class="o">=</span><span class="s">&#39;SAME&#39;</span><span class="p">)</span></span>
<span id="LC140" class="line">            <span class="n">biases</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">Variable</span><span class="p">(</span><span class="n">tf</span><span class="o">.</span><span class="n">constant</span><span class="p">(</span><span class="mf">0.0</span><span class="p">,</span> <span class="n">shape</span><span class="o">=</span><span class="p">[</span><span class="mi">512</span><span class="p">],</span> <span class="n">dtype</span><span class="o">=</span><span class="n">tf</span><span class="o">.</span><span class="n">float32</span><span class="p">),</span></span>
<span id="LC141" class="line">                                 <span class="n">trainable</span><span class="o">=</span><span class="bp">True</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="s">&#39;biases&#39;</span><span class="p">)</span></span>
<span id="LC142" class="line">            <span class="n">out</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">nn</span><span class="o">.</span><span class="n">bias_add</span><span class="p">(</span><span class="n">conv</span><span class="p">,</span> <span class="n">biases</span><span class="p">)</span></span>
<span id="LC143" class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">conv4_1</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">nn</span><span class="o">.</span><span class="n">relu</span><span class="p">(</span><span class="n">out</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="n">scope</span><span class="p">)</span></span>
<span id="LC144" class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">parameters</span> <span class="o">+=</span> <span class="p">[</span><span class="n">kernel</span><span class="p">,</span> <span class="n">biases</span><span class="p">]</span></span>
<span id="LC145" class="line"></span>
<span id="LC146" class="line">        <span class="c"># conv4_2</span></span>
<span id="LC147" class="line">        <span class="k">with</span> <span class="n">tf</span><span class="o">.</span><span class="n">name_scope</span><span class="p">(</span><span class="s">&#39;conv4_2&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">scope</span><span class="p">:</span></span>
<span id="LC148" class="line">            <span class="n">kernel</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">Variable</span><span class="p">(</span><span class="n">tf</span><span class="o">.</span><span class="n">truncated_normal</span><span class="p">([</span><span class="mi">3</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">512</span><span class="p">,</span> <span class="mi">512</span><span class="p">],</span> <span class="n">dtype</span><span class="o">=</span><span class="n">tf</span><span class="o">.</span><span class="n">float32</span><span class="p">,</span></span>
<span id="LC149" class="line">                                                     <span class="n">stddev</span><span class="o">=</span><span class="mf">1e-1</span><span class="p">),</span> <span class="n">name</span><span class="o">=</span><span class="s">&#39;weights&#39;</span><span class="p">)</span></span>
<span id="LC150" class="line">            <span class="n">conv</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">nn</span><span class="o">.</span><span class="n">conv2d</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">conv4_1</span><span class="p">,</span> <span class="n">kernel</span><span class="p">,</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">],</span> <span class="n">padding</span><span class="o">=</span><span class="s">&#39;SAME&#39;</span><span class="p">)</span></span>
<span id="LC151" class="line">            <span class="n">biases</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">Variable</span><span class="p">(</span><span class="n">tf</span><span class="o">.</span><span class="n">constant</span><span class="p">(</span><span class="mf">0.0</span><span class="p">,</span> <span class="n">shape</span><span class="o">=</span><span class="p">[</span><span class="mi">512</span><span class="p">],</span> <span class="n">dtype</span><span class="o">=</span><span class="n">tf</span><span class="o">.</span><span class="n">float32</span><span class="p">),</span></span>
<span id="LC152" class="line">                                 <span class="n">trainable</span><span class="o">=</span><span class="bp">True</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="s">&#39;biases&#39;</span><span class="p">)</span></span>
<span id="LC153" class="line">            <span class="n">out</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">nn</span><span class="o">.</span><span class="n">bias_add</span><span class="p">(</span><span class="n">conv</span><span class="p">,</span> <span class="n">biases</span><span class="p">)</span></span>
<span id="LC154" class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">conv4_2</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">nn</span><span class="o">.</span><span class="n">relu</span><span class="p">(</span><span class="n">out</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="n">scope</span><span class="p">)</span></span>
<span id="LC155" class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">parameters</span> <span class="o">+=</span> <span class="p">[</span><span class="n">kernel</span><span class="p">,</span> <span class="n">biases</span><span class="p">]</span></span>
<span id="LC156" class="line"></span>
<span id="LC157" class="line">        <span class="c"># conv4_3</span></span>
<span id="LC158" class="line">        <span class="k">with</span> <span class="n">tf</span><span class="o">.</span><span class="n">name_scope</span><span class="p">(</span><span class="s">&#39;conv4_3&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">scope</span><span class="p">:</span></span>
<span id="LC159" class="line">            <span class="n">kernel</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">Variable</span><span class="p">(</span><span class="n">tf</span><span class="o">.</span><span class="n">truncated_normal</span><span class="p">([</span><span class="mi">3</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">512</span><span class="p">,</span> <span class="mi">512</span><span class="p">],</span> <span class="n">dtype</span><span class="o">=</span><span class="n">tf</span><span class="o">.</span><span class="n">float32</span><span class="p">,</span></span>
<span id="LC160" class="line">                                                     <span class="n">stddev</span><span class="o">=</span><span class="mf">1e-1</span><span class="p">),</span> <span class="n">name</span><span class="o">=</span><span class="s">&#39;weights&#39;</span><span class="p">)</span></span>
<span id="LC161" class="line">            <span class="n">conv</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">nn</span><span class="o">.</span><span class="n">conv2d</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">conv4_2</span><span class="p">,</span> <span class="n">kernel</span><span class="p">,</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">],</span> <span class="n">padding</span><span class="o">=</span><span class="s">&#39;SAME&#39;</span><span class="p">)</span></span>
<span id="LC162" class="line">            <span class="n">biases</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">Variable</span><span class="p">(</span><span class="n">tf</span><span class="o">.</span><span class="n">constant</span><span class="p">(</span><span class="mf">0.0</span><span class="p">,</span> <span class="n">shape</span><span class="o">=</span><span class="p">[</span><span class="mi">512</span><span class="p">],</span> <span class="n">dtype</span><span class="o">=</span><span class="n">tf</span><span class="o">.</span><span class="n">float32</span><span class="p">),</span></span>
<span id="LC163" class="line">                                 <span class="n">trainable</span><span class="o">=</span><span class="bp">True</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="s">&#39;biases&#39;</span><span class="p">)</span></span>
<span id="LC164" class="line">            <span class="n">out</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">nn</span><span class="o">.</span><span class="n">bias_add</span><span class="p">(</span><span class="n">conv</span><span class="p">,</span> <span class="n">biases</span><span class="p">)</span></span>
<span id="LC165" class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">conv4_3</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">nn</span><span class="o">.</span><span class="n">relu</span><span class="p">(</span><span class="n">out</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="n">scope</span><span class="p">)</span></span>
<span id="LC166" class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">parameters</span> <span class="o">+=</span> <span class="p">[</span><span class="n">kernel</span><span class="p">,</span> <span class="n">biases</span><span class="p">]</span></span>
<span id="LC167" class="line"></span>
<span id="LC168" class="line">        <span class="c"># pool4</span></span>
<span id="LC169" class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">pool4</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">nn</span><span class="o">.</span><span class="n">max_pool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">conv4_3</span><span class="p">,</span></span>
<span id="LC170" class="line">                               <span class="n">ksize</span><span class="o">=</span><span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">1</span><span class="p">],</span></span>
<span id="LC171" class="line">                               <span class="n">strides</span><span class="o">=</span><span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">1</span><span class="p">],</span></span>
<span id="LC172" class="line">                               <span class="n">padding</span><span class="o">=</span><span class="s">&#39;SAME&#39;</span><span class="p">,</span></span>
<span id="LC173" class="line">                               <span class="n">name</span><span class="o">=</span><span class="s">&#39;pool4&#39;</span><span class="p">)</span></span>
<span id="LC174" class="line"></span>
<span id="LC175" class="line">        <span class="c"># conv5_1</span></span>
<span id="LC176" class="line">        <span class="k">with</span> <span class="n">tf</span><span class="o">.</span><span class="n">name_scope</span><span class="p">(</span><span class="s">&#39;conv5_1&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">scope</span><span class="p">:</span></span>
<span id="LC177" class="line">            <span class="n">kernel</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">Variable</span><span class="p">(</span><span class="n">tf</span><span class="o">.</span><span class="n">truncated_normal</span><span class="p">([</span><span class="mi">3</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">512</span><span class="p">,</span> <span class="mi">512</span><span class="p">],</span> <span class="n">dtype</span><span class="o">=</span><span class="n">tf</span><span class="o">.</span><span class="n">float32</span><span class="p">,</span></span>
<span id="LC178" class="line">                                                     <span class="n">stddev</span><span class="o">=</span><span class="mf">1e-1</span><span class="p">),</span> <span class="n">name</span><span class="o">=</span><span class="s">&#39;weights&#39;</span><span class="p">)</span></span>
<span id="LC179" class="line">            <span class="n">conv</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">nn</span><span class="o">.</span><span class="n">conv2d</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">pool4</span><span class="p">,</span> <span class="n">kernel</span><span class="p">,</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">],</span> <span class="n">padding</span><span class="o">=</span><span class="s">&#39;SAME&#39;</span><span class="p">)</span></span>
<span id="LC180" class="line">            <span class="n">biases</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">Variable</span><span class="p">(</span><span class="n">tf</span><span class="o">.</span><span class="n">constant</span><span class="p">(</span><span class="mf">0.0</span><span class="p">,</span> <span class="n">shape</span><span class="o">=</span><span class="p">[</span><span class="mi">512</span><span class="p">],</span> <span class="n">dtype</span><span class="o">=</span><span class="n">tf</span><span class="o">.</span><span class="n">float32</span><span class="p">),</span></span>
<span id="LC181" class="line">                                 <span class="n">trainable</span><span class="o">=</span><span class="bp">True</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="s">&#39;biases&#39;</span><span class="p">)</span></span>
<span id="LC182" class="line">            <span class="n">out</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">nn</span><span class="o">.</span><span class="n">bias_add</span><span class="p">(</span><span class="n">conv</span><span class="p">,</span> <span class="n">biases</span><span class="p">)</span></span>
<span id="LC183" class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">conv5_1</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">nn</span><span class="o">.</span><span class="n">relu</span><span class="p">(</span><span class="n">out</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="n">scope</span><span class="p">)</span></span>
<span id="LC184" class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">parameters</span> <span class="o">+=</span> <span class="p">[</span><span class="n">kernel</span><span class="p">,</span> <span class="n">biases</span><span class="p">]</span></span>
<span id="LC185" class="line"></span>
<span id="LC186" class="line">        <span class="c"># conv5_2</span></span>
<span id="LC187" class="line">        <span class="k">with</span> <span class="n">tf</span><span class="o">.</span><span class="n">name_scope</span><span class="p">(</span><span class="s">&#39;conv5_2&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">scope</span><span class="p">:</span></span>
<span id="LC188" class="line">            <span class="n">kernel</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">Variable</span><span class="p">(</span><span class="n">tf</span><span class="o">.</span><span class="n">truncated_normal</span><span class="p">([</span><span class="mi">3</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">512</span><span class="p">,</span> <span class="mi">512</span><span class="p">],</span> <span class="n">dtype</span><span class="o">=</span><span class="n">tf</span><span class="o">.</span><span class="n">float32</span><span class="p">,</span></span>
<span id="LC189" class="line">                                                     <span class="n">stddev</span><span class="o">=</span><span class="mf">1e-1</span><span class="p">),</span> <span class="n">name</span><span class="o">=</span><span class="s">&#39;weights&#39;</span><span class="p">)</span></span>
<span id="LC190" class="line">            <span class="n">conv</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">nn</span><span class="o">.</span><span class="n">conv2d</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">conv5_1</span><span class="p">,</span> <span class="n">kernel</span><span class="p">,</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">],</span> <span class="n">padding</span><span class="o">=</span><span class="s">&#39;SAME&#39;</span><span class="p">)</span></span>
<span id="LC191" class="line">            <span class="n">biases</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">Variable</span><span class="p">(</span><span class="n">tf</span><span class="o">.</span><span class="n">constant</span><span class="p">(</span><span class="mf">0.0</span><span class="p">,</span> <span class="n">shape</span><span class="o">=</span><span class="p">[</span><span class="mi">512</span><span class="p">],</span> <span class="n">dtype</span><span class="o">=</span><span class="n">tf</span><span class="o">.</span><span class="n">float32</span><span class="p">),</span></span>
<span id="LC192" class="line">                                 <span class="n">trainable</span><span class="o">=</span><span class="bp">True</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="s">&#39;biases&#39;</span><span class="p">)</span></span>
<span id="LC193" class="line">            <span class="n">out</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">nn</span><span class="o">.</span><span class="n">bias_add</span><span class="p">(</span><span class="n">conv</span><span class="p">,</span> <span class="n">biases</span><span class="p">)</span></span>
<span id="LC194" class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">conv5_2</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">nn</span><span class="o">.</span><span class="n">relu</span><span class="p">(</span><span class="n">out</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="n">scope</span><span class="p">)</span></span>
<span id="LC195" class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">parameters</span> <span class="o">+=</span> <span class="p">[</span><span class="n">kernel</span><span class="p">,</span> <span class="n">biases</span><span class="p">]</span></span>
<span id="LC196" class="line"></span>
<span id="LC197" class="line">        <span class="c"># conv5_3</span></span>
<span id="LC198" class="line">        <span class="k">with</span> <span class="n">tf</span><span class="o">.</span><span class="n">name_scope</span><span class="p">(</span><span class="s">&#39;conv5_3&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">scope</span><span class="p">:</span></span>
<span id="LC199" class="line">            <span class="n">kernel</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">Variable</span><span class="p">(</span><span class="n">tf</span><span class="o">.</span><span class="n">truncated_normal</span><span class="p">([</span><span class="mi">3</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">512</span><span class="p">,</span> <span class="mi">512</span><span class="p">],</span> <span class="n">dtype</span><span class="o">=</span><span class="n">tf</span><span class="o">.</span><span class="n">float32</span><span class="p">,</span></span>
<span id="LC200" class="line">                                                     <span class="n">stddev</span><span class="o">=</span><span class="mf">1e-1</span><span class="p">),</span> <span class="n">name</span><span class="o">=</span><span class="s">&#39;weights&#39;</span><span class="p">)</span></span>
<span id="LC201" class="line">            <span class="n">conv</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">nn</span><span class="o">.</span><span class="n">conv2d</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">conv5_2</span><span class="p">,</span> <span class="n">kernel</span><span class="p">,</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">],</span> <span class="n">padding</span><span class="o">=</span><span class="s">&#39;SAME&#39;</span><span class="p">)</span></span>
<span id="LC202" class="line">            <span class="n">biases</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">Variable</span><span class="p">(</span><span class="n">tf</span><span class="o">.</span><span class="n">constant</span><span class="p">(</span><span class="mf">0.0</span><span class="p">,</span> <span class="n">shape</span><span class="o">=</span><span class="p">[</span><span class="mi">512</span><span class="p">],</span> <span class="n">dtype</span><span class="o">=</span><span class="n">tf</span><span class="o">.</span><span class="n">float32</span><span class="p">),</span></span>
<span id="LC203" class="line">                                 <span class="n">trainable</span><span class="o">=</span><span class="bp">True</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="s">&#39;biases&#39;</span><span class="p">)</span></span>
<span id="LC204" class="line">            <span class="n">out</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">nn</span><span class="o">.</span><span class="n">bias_add</span><span class="p">(</span><span class="n">conv</span><span class="p">,</span> <span class="n">biases</span><span class="p">)</span></span>
<span id="LC205" class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">conv5_3</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">nn</span><span class="o">.</span><span class="n">relu</span><span class="p">(</span><span class="n">out</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="n">scope</span><span class="p">)</span></span>
<span id="LC206" class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">parameters</span> <span class="o">+=</span> <span class="p">[</span><span class="n">kernel</span><span class="p">,</span> <span class="n">biases</span><span class="p">]</span></span>
<span id="LC207" class="line"></span>
<span id="LC208" class="line">        <span class="c"># pool5</span></span>
<span id="LC209" class="line">        <span class="bp">self</span><span class="o">.</span><span class="n">pool5</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">nn</span><span class="o">.</span><span class="n">max_pool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">conv5_3</span><span class="p">,</span></span>
<span id="LC210" class="line">                               <span class="n">ksize</span><span class="o">=</span><span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">1</span><span class="p">],</span></span>
<span id="LC211" class="line">                               <span class="n">strides</span><span class="o">=</span><span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">1</span><span class="p">],</span></span>
<span id="LC212" class="line">                               <span class="n">padding</span><span class="o">=</span><span class="s">&#39;SAME&#39;</span><span class="p">,</span></span>
<span id="LC213" class="line">                               <span class="n">name</span><span class="o">=</span><span class="s">&#39;pool4&#39;</span><span class="p">)</span></span>
<span id="LC214" class="line"></span>
<span id="LC215" class="line">    <span class="k">def</span> <span class="nf">fc_layers</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span>
<span id="LC216" class="line">        <span class="c"># fc1</span></span>
<span id="LC217" class="line">        <span class="k">with</span> <span class="n">tf</span><span class="o">.</span><span class="n">name_scope</span><span class="p">(</span><span class="s">&#39;fc1&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">scope</span><span class="p">:</span></span>
<span id="LC218" class="line">            <span class="n">shape</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">prod</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">pool5</span><span class="o">.</span><span class="n">get_shape</span><span class="p">()[</span><span class="mi">1</span><span class="p">:]))</span></span>
<span id="LC219" class="line">            <span class="n">fc1w</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">Variable</span><span class="p">(</span><span class="n">tf</span><span class="o">.</span><span class="n">truncated_normal</span><span class="p">([</span><span class="n">shape</span><span class="p">,</span> <span class="mi">4096</span><span class="p">],</span></span>
<span id="LC220" class="line">                                                         <span class="n">dtype</span><span class="o">=</span><span class="n">tf</span><span class="o">.</span><span class="n">float32</span><span class="p">,</span></span>
<span id="LC221" class="line">                                                         <span class="n">stddev</span><span class="o">=</span><span class="mf">1e-1</span><span class="p">),</span> <span class="n">name</span><span class="o">=</span><span class="s">&#39;weights&#39;</span><span class="p">)</span></span>
<span id="LC222" class="line">            <span class="n">fc1b</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">Variable</span><span class="p">(</span><span class="n">tf</span><span class="o">.</span><span class="n">constant</span><span class="p">(</span><span class="mf">1.0</span><span class="p">,</span> <span class="n">shape</span><span class="o">=</span><span class="p">[</span><span class="mi">4096</span><span class="p">],</span> <span class="n">dtype</span><span class="o">=</span><span class="n">tf</span><span class="o">.</span><span class="n">float32</span><span class="p">),</span></span>
<span id="LC223" class="line">                                 <span class="n">trainable</span><span class="o">=</span><span class="bp">True</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="s">&#39;biases&#39;</span><span class="p">)</span></span>
<span id="LC224" class="line">            <span class="n">pool5_flat</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">reshape</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">pool5</span><span class="p">,</span> <span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">,</span> <span class="n">shape</span><span class="p">])</span></span>
<span id="LC225" class="line">            <span class="n">fc1l</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">nn</span><span class="o">.</span><span class="n">bias_add</span><span class="p">(</span><span class="n">tf</span><span class="o">.</span><span class="n">matmul</span><span class="p">(</span><span class="n">pool5_flat</span><span class="p">,</span> <span class="n">fc1w</span><span class="p">),</span> <span class="n">fc1b</span><span class="p">)</span></span>
<span id="LC226" class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">fc1</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">nn</span><span class="o">.</span><span class="n">relu</span><span class="p">(</span><span class="n">fc1l</span><span class="p">)</span></span>
<span id="LC227" class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">parameters</span> <span class="o">+=</span> <span class="p">[</span><span class="n">fc1w</span><span class="p">,</span> <span class="n">fc1b</span><span class="p">]</span></span>
<span id="LC228" class="line"></span>
<span id="LC229" class="line">        <span class="c"># fc2</span></span>
<span id="LC230" class="line">        <span class="k">with</span> <span class="n">tf</span><span class="o">.</span><span class="n">name_scope</span><span class="p">(</span><span class="s">&#39;fc2&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">scope</span><span class="p">:</span></span>
<span id="LC231" class="line">            <span class="n">fc2w</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">Variable</span><span class="p">(</span><span class="n">tf</span><span class="o">.</span><span class="n">truncated_normal</span><span class="p">([</span><span class="mi">4096</span><span class="p">,</span> <span class="mi">4096</span><span class="p">],</span></span>
<span id="LC232" class="line">                                                         <span class="n">dtype</span><span class="o">=</span><span class="n">tf</span><span class="o">.</span><span class="n">float32</span><span class="p">,</span></span>
<span id="LC233" class="line">                                                         <span class="n">stddev</span><span class="o">=</span><span class="mf">1e-1</span><span class="p">),</span> <span class="n">name</span><span class="o">=</span><span class="s">&#39;weights&#39;</span><span class="p">)</span></span>
<span id="LC234" class="line">            <span class="n">fc2b</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">Variable</span><span class="p">(</span><span class="n">tf</span><span class="o">.</span><span class="n">constant</span><span class="p">(</span><span class="mf">1.0</span><span class="p">,</span> <span class="n">shape</span><span class="o">=</span><span class="p">[</span><span class="mi">4096</span><span class="p">],</span> <span class="n">dtype</span><span class="o">=</span><span class="n">tf</span><span class="o">.</span><span class="n">float32</span><span class="p">),</span></span>
<span id="LC235" class="line">                                 <span class="n">trainable</span><span class="o">=</span><span class="bp">True</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="s">&#39;biases&#39;</span><span class="p">)</span></span>
<span id="LC236" class="line">            <span class="n">fc2l</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">nn</span><span class="o">.</span><span class="n">bias_add</span><span class="p">(</span><span class="n">tf</span><span class="o">.</span><span class="n">matmul</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">fc1</span><span class="p">,</span> <span class="n">fc2w</span><span class="p">),</span> <span class="n">fc2b</span><span class="p">)</span></span>
<span id="LC237" class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">fc2</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">nn</span><span class="o">.</span><span class="n">relu</span><span class="p">(</span><span class="n">fc2l</span><span class="p">)</span></span>
<span id="LC238" class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">parameters</span> <span class="o">+=</span> <span class="p">[</span><span class="n">fc2w</span><span class="p">,</span> <span class="n">fc2b</span><span class="p">]</span></span>
<span id="LC239" class="line"></span>
<span id="LC240" class="line">        <span class="c"># fc3</span></span>
<span id="LC241" class="line">        <span class="k">with</span> <span class="n">tf</span><span class="o">.</span><span class="n">name_scope</span><span class="p">(</span><span class="s">&#39;fc3&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">scope</span><span class="p">:</span></span>
<span id="LC242" class="line">            <span class="n">fc3w</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">Variable</span><span class="p">(</span><span class="n">tf</span><span class="o">.</span><span class="n">truncated_normal</span><span class="p">([</span><span class="mi">4096</span><span class="p">,</span> <span class="mi">1000</span><span class="p">],</span></span>
<span id="LC243" class="line">                                                         <span class="n">dtype</span><span class="o">=</span><span class="n">tf</span><span class="o">.</span><span class="n">float32</span><span class="p">,</span></span>
<span id="LC244" class="line">                                                         <span class="n">stddev</span><span class="o">=</span><span class="mf">1e-1</span><span class="p">),</span> <span class="n">name</span><span class="o">=</span><span class="s">&#39;weights&#39;</span><span class="p">)</span></span>
<span id="LC245" class="line">            <span class="n">fc3b</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">Variable</span><span class="p">(</span><span class="n">tf</span><span class="o">.</span><span class="n">constant</span><span class="p">(</span><span class="mf">1.0</span><span class="p">,</span> <span class="n">shape</span><span class="o">=</span><span class="p">[</span><span class="mi">1000</span><span class="p">],</span> <span class="n">dtype</span><span class="o">=</span><span class="n">tf</span><span class="o">.</span><span class="n">float32</span><span class="p">),</span></span>
<span id="LC246" class="line">                                 <span class="n">trainable</span><span class="o">=</span><span class="bp">True</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="s">&#39;biases&#39;</span><span class="p">)</span></span>
<span id="LC247" class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">fc3l</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">nn</span><span class="o">.</span><span class="n">bias_add</span><span class="p">(</span><span class="n">tf</span><span class="o">.</span><span class="n">matmul</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">fc2</span><span class="p">,</span> <span class="n">fc3w</span><span class="p">),</span> <span class="n">fc3b</span><span class="p">)</span></span>
<span id="LC248" class="line">            <span class="bp">self</span><span class="o">.</span><span class="n">parameters</span> <span class="o">+=</span> <span class="p">[</span><span class="n">fc3w</span><span class="p">,</span> <span class="n">fc3b</span><span class="p">]</span></span>
<span id="LC249" class="line"></span>
<span id="LC250" class="line">    <span class="k">def</span> <span class="nf">load_weights</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">weight_file</span><span class="p">,</span> <span class="n">sess</span><span class="p">):</span></span>
<span id="LC251" class="line">        <span class="n">weights</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="n">weight_file</span><span class="p">)</span></span>
<span id="LC252" class="line">        <span class="n">keys</span> <span class="o">=</span> <span class="nb">sorted</span><span class="p">(</span><span class="n">weights</span><span class="o">.</span><span class="n">keys</span><span class="p">())</span></span>
<span id="LC253" class="line">        <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">k</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">keys</span><span class="p">):</span></span>
<span id="LC254" class="line">            <span class="c"># XXX wingated</span></span>
<span id="LC255" class="line">            <span class="c"># if k[0:2] == &quot;fc&quot;:  # skip loading FC layers</span></span>
<span id="LC256" class="line">            <span class="c">#     continue</span></span>
<span id="LC257" class="line">            <span class="c"># print i, k, np.shape(weights[k])</span></span>
<span id="LC258" class="line">            <span class="n">sess</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">parameters</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="o">.</span><span class="n">assign</span><span class="p">(</span><span class="n">weights</span><span class="p">[</span><span class="n">k</span><span class="p">]))</span></span>
<span id="LC259" class="line"></span>
<span id="LC260" class="line"><span class="c"># XXX wingated</span></span>
<span id="LC261" class="line"><span class="c"># if __name__ == &#39;__main__&#39;:</span></span>
<span id="LC262" class="line"><span class="c">#     sess = tf.Session()</span></span>
<span id="LC263" class="line"><span class="c">#     imgs = tf.placeholder(tf.float32, [None, 224, 224, 3])</span></span>
<span id="LC264" class="line"><span class="c">#     vgg = vgg16(imgs, &#39;vgg16_weights.npz&#39;, sess)</span></span>
<span id="LC265" class="line"></span>
<span id="LC266" class="line"><span class="c">#     img1 = imread(&#39;laska.png&#39;, mode=&#39;RGB&#39;)</span></span>
<span id="LC267" class="line"><span class="c">#     img1 = imresize(img1, (224, 224))</span></span>
<span id="LC268" class="line"></span>
<span id="LC269" class="line"><span class="c">#     prob = sess.run(vgg.probs, feed_dict={vgg.imgs: [img1]})[0]</span></span>
<span id="LC270" class="line"><span class="c">#     preds = (np.argsort(prob)[::-1])[0:5]</span></span>
<span id="LC271" class="line"><span class="c">#     for p in preds:</span></span>
<span id="LC272" class="line"><span class="c">#         print class_names[p], prob[p]</span></span></code></pre>

</div>
</div>


</article>
</div>

</div>
<div class='modal' id='modal-remove-blob'>
<div class='modal-dialog'>
<div class='modal-content'>
<div class='modal-header'>
<a class='close' data-dismiss='modal' href='#'>×</a>
<h3 class='page-title'>Delete vgg16.py</h3>
</div>
<div class='modal-body'>
<form class="form-horizontal js-replace-blob-form js-quick-submit js-requires-input" action="/gitlab/gellings/im2att_tf/blob/master/vgg16.py" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="_method" value="delete" /><input type="hidden" name="authenticity_token" value="16MRArvy3VROKe3UT+q6RYta64kKRRXJEWHwXF2/X3niVhW6CzM9RvcNwGW1yP/XsUO4RAb74/gZl7MXzs458Q==" />
<div class='form-group commit_message-group'>
<label class="control-label" for="commit_message-9b746ed6149bc91d7c3ba8b401636b90">Commit message
</label><div class='col-sm-10'>
<div class='commit-message-container'>
<div class='max-width-marker'></div>
<textarea name="commit_message" id="commit_message-9b746ed6149bc91d7c3ba8b401636b90" class="form-control js-commit-message" placeholder="Delete vgg16.py" required="required" rows="3">
</textarea>
</div>
</div>
</div>

<div class='form-group branch'>
<label class="control-label" for="target_branch">Target branch</label>
<div class='col-sm-10'>
<input type="text" name="target_branch" id="target_branch" value="master" required="required" class="form-control js-target-branch" />
<div class='js-create-merge-request-container'>
<div class='checkbox'>
<label for="create_merge_request-fd3f0d4d870c64ce2f75fc7ebf2b130b"><input type="checkbox" name="create_merge_request" id="create_merge_request-fd3f0d4d870c64ce2f75fc7ebf2b130b" value="1" class="js-create-merge-request" checked="checked" />
Start a <strong>new merge request</strong> with these changes
</label></div>
</div>
</div>
</div>
<input type="hidden" name="original_branch" id="original_branch" value="master" class="js-original-branch" />

<div class='form-group'>
<div class='col-sm-offset-2 col-sm-10'>
<button name="button" type="submit" class="btn btn-remove btn-remove-file">Delete file</button>
<a class="btn btn-cancel" data-dismiss="modal" href="#">Cancel</a>
</div>
</div>
</form>

</div>
</div>
</div>
</div>
<script>
  new NewCommitForm($('.js-replace-blob-form'))
</script>

<div class='modal' id='modal-upload-blob'>
<div class='modal-dialog'>
<div class='modal-content'>
<div class='modal-header'>
<a class='close' data-dismiss='modal' href='#'>×</a>
<h3 class='page-title'>Replace vgg16.py</h3>
</div>
<div class='modal-body'>
<form class="js-quick-submit js-upload-blob-form form-horizontal" action="/gitlab/gellings/im2att_tf/update/master/vgg16.py" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="_method" value="put" /><input type="hidden" name="authenticity_token" value="/NQ/9pko7EXUPcu9RlS5C1EJotkJ8hRRr+WRpb9ZoazJITtOKekMV20Z5gy8dvyZaxDxFAVM4mCnE9LuLCjHJA==" />
<div class='dropzone'>
<div class='dropzone-previews blob-upload-dropzone-previews'>
<p class='dz-message light'>
Attach a file by drag &amp; drop or
<a class="markdown-selector" href="#">click to upload</a>
</p>
</div>
</div>
<br>
<div class='alert alert-danger data dropzone-alerts' style='display:none'></div>
<div class='form-group commit_message-group'>
<label class="control-label" for="commit_message-11bf485d6da2391b6e2445f61b109dc2">Commit message
</label><div class='col-sm-10'>
<div class='commit-message-container'>
<div class='max-width-marker'></div>
<textarea name="commit_message" id="commit_message-11bf485d6da2391b6e2445f61b109dc2" class="form-control js-commit-message" placeholder="Replace vgg16.py" required="required" rows="3">
</textarea>
</div>
</div>
</div>

<div class='form-group branch'>
<label class="control-label" for="target_branch">Target branch</label>
<div class='col-sm-10'>
<input type="text" name="target_branch" id="target_branch" value="master" required="required" class="form-control js-target-branch" />
<div class='js-create-merge-request-container'>
<div class='checkbox'>
<label for="create_merge_request-dbae20b640a40d847442ba1b2bcd3034"><input type="checkbox" name="create_merge_request" id="create_merge_request-dbae20b640a40d847442ba1b2bcd3034" value="1" class="js-create-merge-request" checked="checked" />
Start a <strong>new merge request</strong> with these changes
</label></div>
</div>
</div>
</div>
<input type="hidden" name="original_branch" id="original_branch" value="master" class="js-original-branch" />

<div class='form-actions'>
<button name="button" type="submit" class="btn btn-small btn-create btn-upload-file" id="submit-all">Replace file</button>
<a class="btn btn-cancel" data-dismiss="modal" href="#">Cancel</a>
</div>
</form>

</div>
</div>
</div>
</div>
<script>
  disableButtonIfEmptyField($('.js-upload-blob-form').find('.js-commit-message'), '.btn-upload-file');
  new BlobFileDropzone($('.js-upload-blob-form'), 'put');
  new NewCommitForm($('.js-upload-blob-form'))
</script>


</div>
</div>
</div>
</div>
</div>



</body>
</html>

