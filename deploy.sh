#!/bin/sh

scp *.py pozitron@jenkins-master.int.pozitron.com:/home/pozitron
scp hubble.sh pozitron@jenkins-master.int.pozitron.com:/home/pozitron

echo ""
echo "1. ssh to jenkins-master"
echo "2. copy *.py and hubble.sh into /mnt/jenkins/slaves/android/helpers"
echo "3. restart android slaves"
echo ""