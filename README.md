# android project summary
Aggregates various android project information and generates json.

# Why?
If you sit on bunch of android apps you may find yourself or your teammates asking questions like, 
Are we targeting 23 on project x? What's the usage of gradle plugin 1.3.1 in our projects? Which of 
our projects are asking GET_ACCOUNTS? Do we have any app with minSdk different than 19? and many 
many more...
 
With this work and additional ones to come in near future, we're trying to come to a point where we 
can list/filter our projects based on any parameter and see a brief summary.

# How?
Combines parsed and processed gradle build files, data read with aapt and some jenkins environment 
information.

# When?
As part of our internal build process, the summary information is generated during a jenkins prod build 
job as a post build step.
 
# What's next?
Simple lovely summary rest api - projects info display based on any property
Display of data in a lovely way

# Generated Json

'''json
{
    "apk": {
        "methodCount": 40046, 
        "versionName": "1.4.0", 
        "minSdk": 19, 
        "appId": "com.pozitron.sample.localDebug", 
        "versionCode": 8, 
        "apkSize": "14.0", 
        "buildVariant": "prod-release", 
        "targetSdk": 22, 
        "permissions": [
            "uses-permission: name='android.permission.INTERNET'", 
            "uses-permission: name='android.permission.ACCESS_NETWORK_STATE'", 
            "uses-permission: name='android.permission.WAKE_LOCK'", 
            "uses-permission: name='com.google.android.c2dm.permission.RECEIVE'", 
            "uses-permission: name='android.permission.GET_ACCOUNTS' maxSdkVersion='18'", 
            "uses-permission: name='android.permission.BLUETOOTH'", 
            "uses-permission: name='android.permission.BLUETOOTH_ADMIN'", 
            "uses-permission: name='android.permission.RECEIVE_BOOT_COMPLETED'", 
            "uses-permission: name='android.permission.ACCESS_COARSE_LOCATION'", 
            "uses-permission: name='android.permission.ACCESS_FINE_LOCATION'", 
            "uses-permission: name='android.permission.READ_PHONE_STATE'", 
            "uses-permission: name='android.permission.WRITE_EXTERNAL_STORAGE'", 
            "permission: com.pozitron.sample.localDebug.permission.C2D_MESSAGE", 
            "uses-permission: name='com.pozitron.pegasus.localDebug.permission.C2D_MESSAGE'", 
            "uses-permission: name='android.permission.READ_EXTERNAL_STORAGE'"
        ]
    }, 
    "build": {
            "compileSdkVersion": "23", 
            "buildToolsVersion": "23.0.3",
        "deps": [
            {
                "group": "com.android.support", 
                "version": "23.3.0", 
                "config": "compile", 
                "name": "appcompat-v7", 
                "module": "app"
            }, 
            {
                "group": "com.android.support", 
                "version": "23.3.0", 
                "config": "compile", 
                "name": "cardview-v7", 
                "module": "app"
            }, 
            {
                "group": "com.android.support", 
                "version": "23.3.0", 
                "config": "compile", 
                "name": "recyclerview-v7", 
                "module": "app"
            }, 
            {
                "group": "com.android.support", 
                "version": "23.3.0", 
                "config": "compile", 
                "name": "design", 
                "module": "app"
            }, 
            {
                "group": "com.canelmas.deps", 
                "version": "2.2.0@aar", 
                "config": "compile", 
                "name": "lovely-core", 
                "module": "app"
            }, 
            {
                "group": "com.canelmas.deps", 
                "version": "2.0.0@aar", 
                "config": "compile", 
                "name": "loveley-ui", 
                "module": "app"
            }, 
            {
                "group": "com.canelmas.deps", 
                "version": "3.1.0@aar", 
                "config": "compile", 
                "name": "loveley-mvp", 
                "module": "app"
            }, 
            {
                "group": "com.canelmas.deps", 
                "version": "3.3.0@aar", 
                "config": "compile", 
                "name": "lovely-util", 
               "module": "app"
            }, 
            {
                "group": "com.canelmas.deps", 
                "version": "1.0.0", 
                "config": "compile", 
                "name": "lovellyfit", 
                "module": "app"
            }, 
            {
                "group": "com.canelmas.deps", 
                "version": "1.0.0", 
                "config": "compile", 
                "name": "lovelybus", 
                "module": "app"
            }, 
            {
                "group": "com.crashlytics.sdk.android", 
                "version": "2.5.5@aar", 
                "config": "compile", 
                "name": "crashlytics", 
                "module": "app"
            }, 
            {
                "group": "com.google.android.gms", 
                "version": "9.0.2", 
                "config": "compile", 
                "name": "play-services-base", 
                "module": "app"
            }, 
            {
                "group": "com.google.android.gms", 
                "version": "9.0.2", 
                "config": "compile", 
                "name": "play-services-analytics", 
                "module": "app"
            }, 
            {
                "group": "com.google.firebase", 
                "version": "7.7.7", 
                "config": "compile", 
                "name": "firebase-core", 
                "module": "app"
            }, 
            {
                "group": "com.google.firebase", 
                "version": "7.7.7", 
                "config": "compile", 
                "name": "firebase-messaging", 
                "module": "app"
            }, 
            {
                "group": "com.google.dagger", 
                "version": "2.2", 
                "config": "apt", 
                "name": "dagger-compiler", 
                "module": "app"
            }, 
            {
                "group": "com.google.dagger", 
                "version": "2.2", 
                "config": "compile", 
                "name": "dagger", 
                "module": "sample/app"
            }, 
            {
                "group": "org.glassfish", 
                "version": "10.0-b28", 
                "config": "provided", 
                "name": "javax.annotation", 
                "module": "app"
            }, 
            {
                "group": "com.jakewharton", 
                "version": "8.0.1", 
                "config": "compile", 
                "name": "butterknife", 
                "module": "app"
            }, 
            {
                "group": "com.jakewharton", 
                "version": "8.0.1", 
                "config": "apt", 
                "name": "butterknife-compiler", 
                "module": "app"
            }, 
            {
                "group": "org.greenrobot", 
                "version": "3.0.0", 
                "config": "compile", 
                "name": "eventbus", 
                "module": "app"
            }, 
            {
                "group": "com.hannesdorfmann.fragmentargs", 
                "version": "3.0.2", 
                "config": "compile", 
                "name": "annotation", 
                "module": "app"
            }, 
            {
                "group": "com.hannesdorfmann.fragmentargs", 
                "version": "3.0.2", 
                "config": "apt", 
                "name": "processor", 
                "module": "app"
            }, 
            {
                "group": "frankiesardo", 
                "version": "3.2.0", 
                "config": "compile", 
                "name": "icepick", 
                "module": "app"
            }, 
            {
                "group": "frankiesardo", 
                "version": "3.2.0", 
                "config": "provided", 
                "name": "icepick-processor", 
                "module": "sample/app"
            }, 
            {
                "group": "net.danlew", 
                "version": "2.9.3.1", 
                "config": "compile", 
                "name": "android.joda", 
                "module": "app"
            }, 
            {
                "group": "com.timehop.stickyheadersrecyclerview", 
                "version": "0.4.3", 
                "config": "compile", 
                "name": "library", 
                "module": "app"
            }, 
            {
                "group": "com.ogaclejapan.smarttablayout", 
                "version": "1.6.1@aar", 
                "config": "compile", 
                "name": "library", 
                "module": "app"
            }, 
            {
                "group": "com.facebook.fresco", 
                "version": "0.10.0", 
                "config": "compile", 
                "name": "fresco", 
                "module": "app"
            }, 
            {
                "group": "io.reactivex", 
                "version": "1.1.5", 
                "config": "compile", 
                "name": "rxjava", 
                "module": "app"
            }, 
            {
                "group": "io.reactivex", 
                "version": "1.2.0", 
                "config": "compile", 
                "name": "rxandroid", 
                "module": "lib"
            }, 
            {
                "group": "com.jakewharton.rxbinding", 
                "version": "0.4.0", 
                "config": "compile", 
                "name": "rxbinding-appcompat-v7", 
                "module": "lib"
            }, 
            {
                "group": "com.android.support", 
                "version": "23.3.0", 
                "config": "compile", 
                "name": "appcompat-v7", 
                "module": "lib"
            }, 
            {
                "group": "com.android.support", 
                "version": "23.3.0", 
                "config": "compile", 
                "name": "cardview-v7", 
                "module": "lib"
            }, 
            {
                "group": "com.android.support", 
                "version": "23.3.0", 
                "config": "compile", 
                "name": "recyclerview-v7", 
                "module": "lib"
            }, 
            {
                "group": "com.android.support", 
                "version": "23.3.0", 
                "config": "compile", 
                "name": "design", 
                "module": "lib"
            }, 
            {
                "group": "com.google.android.gms", 
                "version": "9.0.2", 
                "config": "compile", 
                "name": "play-services-base", 
                "module": "lib"
            }, 
            {
                "group": "com.google.android.gms", 
                "version": "9.0.2", 
                "config": "compile", 
                "name": "play-services-analytics", 
                "module": "lib"
            }, 
            {
                "group": "com.google.firebase", 
                "version": "7.7.7", 
                "config": "compile", 
                "name": "firebase-core", 
                "module": "lib"
            }, 
            {
                "group": "com.google.firebase", 
                "version": "7.7.7", 
                "config": "compile", 
                "name": "firebase-messaging", 
                "module": "lib"
            }, 
            {
                "group": "io.reactivex", 
                "version": "1.1.5", 
                "config": "compile", 
                "name": "rxjava", 
                "module": "lib"
            }, 
            {
                "group": "com.jakewharton.rxbinding", 
                "version": "0.4.0", 
                "config": "compile", 
                "name": "rxbinding-appcompat-v7", 
                "module": "lib"
            }, 
            {
                "group": "org.hibernate", 
                "version": "3.0.5", 
                "config": "runtime", 
                "name": "hibernate", 
                "module": "lib"
            }, 
            {
                "group": "org.hibernate", 
                "version": "3.0.5", 
                "config": "runtime", 
                "name": "hibernate", 
                "module": "lib"
            }
        ], 
        "classpath": [
            {
                "group": "com.android.tools.build", 
                "version": "2.1.2", 
                "config": "classpath", 
                "name": "gradle"
            }, 
            {
                "group": "com.neenbedankt.gradle.plugins", 
                "version": "1.8", 
                "config": "classpath", 
                "name": "android-apt"
            }, 
            {
                "group": "com.google.gms", 
                "version": "3.0.0", 
                "config": "classpath", 
                "name": "google-services"
            }
        ]        
    }, 
   "jenkins": {
        "node": "jenkins-android-3",
        "commit": "8f2e682c359688129803cc85c1ee2c05d97f5b14",
        "url": "ssh://jenkins@gerrit.pozitron.com:29418/XXXX-Android",
        "id": "6",
        "branch": "master"
    }

}

'''