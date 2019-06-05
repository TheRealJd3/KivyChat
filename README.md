# Steps for Android Deployment
1. Get buildozer (pip3 install buildozer)
2. sudo apt-get install automake autoconf libltdl-dev to avoid some errors
3. buildozer init in directory
4. Edit buildozer spec as required by the application (For example, chat app requires internet connection, so uncomment the android internet bit)
5. buildozer -v android debug deploy run

buildozer -v android debug deploy run = VERBOSE FORM

Needed to accept some dialog which would not show up without the flag and would mess up the deployment.
