Name:           ros-indigo-roslisp-repl
Version:        0.4.10
Release:        0%{?dist}
Summary:        ROS roslisp_repl package

Group:          Development/Libraries
License:        Public domain
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-rosemacs
Requires:       ros-indigo-roslisp
Requires:       ros-indigo-slime-ros
Requires:       ros-indigo-slime-wrapper
Requires:       sbcl
BuildRequires:  ros-indigo-catkin

%description
This package provides a script that launches Emacs with Slime (the Superior Lisp
Interaction Mode) ready for Lisp development and roslisp.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon Aug 22 2016 Gayane Kazhoyan <kazhoyan@cs.uni-bremen.de> - 0.4.10-0
- Autogenerated by Bloom

* Tue Dec 22 2015 Gayane Kazhoyan <kazhoyan@cs.uni-bremen.de> - 0.4.9-0
- Autogenerated by Bloom

* Wed Sep 16 2015 Gayane Kazhoyan <kazhoyan@cs.uni-bremen.de> - 0.4.8-0
- Autogenerated by Bloom

* Mon Jun 01 2015 Gayane Kazhoyan <kazhoyan@cs.uni-bremen.de> - 0.4.7-1
- Autogenerated by Bloom

* Mon Jun 01 2015 Gayane Kazhoyan <kazhoyan@cs.uni-bremen.de> - 0.4.7-0
- Autogenerated by Bloom

* Thu Feb 12 2015 Gayane Kazhoyan <kazhoyan@cs.uni-bremen.de> - 0.4.6-0
- Autogenerated by Bloom

* Mon Nov 17 2014 Gayane Kazhoyan <kazhoyan@cs.uni-bremen.de> - 0.4.5-0
- Autogenerated by Bloom

* Thu Nov 06 2014 Gayane Kazhoyan <kazhoyan@cs.uni-bremen.de> - 0.4.4-0
- Autogenerated by Bloom

* Thu Nov 06 2014 Gayane Kazhoyan <kazhoyan@cs.uni-bremen.de> - 0.4.3-1
- Autogenerated by Bloom

* Fri Sep 26 2014 Gayane Kazhoyan <kazhoyan@cs.uni-bremen.de> - 0.4.3-0
- Autogenerated by Bloom

* Tue Sep 09 2014 Gayane Kazhoyan <kazhoyan@cs.uni-bremen.de> - 0.4.2-0
- Autogenerated by Bloom

* Thu Sep 04 2014 Gayane Kazhoyan <kazhoyan@cs.uni-bremen.de> - 0.4.1-3
- Autogenerated by Bloom

* Thu Sep 04 2014 Gayane Kazhoyan <kazhoyan@cs.uni-bremen.de> - 0.4.1-2
- Autogenerated by Bloom

* Thu Sep 04 2014 Gayane Kazhoyan <kazhoyan@cs.uni-bremen.de> - 0.4.1-1
- Autogenerated by Bloom

* Thu Sep 04 2014 Gayane Kazhoyan <kazhoyan@cs.uni-bremen.de> - 0.4.1-0
- Autogenerated by Bloom

