civicrm_tarl10n
===============

Creates a CiviCRM tarball with customised localisation (l10n), ownership, permissions etc.

Background
----------

Each new CiviCRM release, I found myself jumping through the same hoops after downloading the tar files.  I have only tested with Drupal flavoured tarfiles, so far.


Requirements
------------
Just standard python needed.


Run
---
Download civicrm-x.y.z-drupal.tar.gz and civicrm-x.y.z-l10n.tar.gz.

python civicrm_tarl10n.py \

       -i civicrm-x.y.z-drupal.tar.gz \

       -l civicrm-x.y.z-l10n.tar.gz   \

       -o civicrm-x.y.z-custom.tar.gz \

       -u www-data -g www-data        \

       -f 0640 -d 0750                \

       -c en_GB -c fr_CA

For more details, python civicrm_tarl10n.py -h
