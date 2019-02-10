# perm_StreamlabsParameter

A parameter for checking if a user has a permission level

## Requirements

You need python scripting set up for Streamlabs Chatbot.  This means you must
have Python 2.7.13 installed.  There are tutorials available online for
installing Python and configuring Streamlabs Chatbot to use it.

## Installation

You can download the .ZIP file for this script from the repository page at
https://github.com/madelsberger/perm_StreamlabsParameter

(Near the top right of the page, click the **Clone or Download** button; in the
pop-up, click **Download ZIP**.)

Then on the Scripts tab in Streamlabs Chatbot, click the import button (an
"arrow-pointing-into-a-box" icon near the upper right of the screen) and select
the downloaded zip file.

The script list should now include *perm*; check the **Enabled** box for this
script, and it will be ready to use in commands.

## Usage

Once you import this script, you can use the $perm parameter in your commands.  
The parameter syntax is

    $perm(<user>, <permission>)

and it will evaluate to 1 if the user has the specified permission, or 0
otherwise.  (This is to make $perm work well with $if, which is its main use
case; see the examples below.  You can find the script for $if at
https://github.com/madelsberger/if_StreamlabsParameter)

This is built on the Parent.HasPermission method used in Python scripting and
so recognizes any <permission> recognized by that method.

(Developer note: as of this writing, I cannot locate detailed documentation of
recognized permission levels.  I'd swear I'd found a list in the past, and in 
my scripts I have used 

  Everyone
  Regular
  Subscriber
  Moderator
  Editor
  Caster

I believe VIP-related permissions have been added recently as well.  I will
update this documentation if I'm again able to find a definitive source.)

For example

    $perm(madelsberger, Subscriber)

would evaluate to either 1 or 0.  This response may seem silly, but it makes
$perm work as the first parameter to the $if parameter (see
https://github.com/madelsberger/if_StreamlabsParameter):

    $if('$perm(madelsberger, Subscriber)', 'Thanks for your support', ':(')
