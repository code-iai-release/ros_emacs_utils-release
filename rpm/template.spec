%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-ros-emacs-utils
Version:        0.4.15
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS ros_emacs_utils package

License:        BSD
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-noetic-rosemacs
Requires:       ros-noetic-roslisp-repl
Requires:       ros-noetic-slime-ros
Requires:       ros-noetic-slime-wrapper
BuildRequires:  ros-noetic-catkin
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
A metapackage of Emacs utils for ROS. Only there for simplifying the release
process.

%prep
%autosetup

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_LIBDIR="lib" \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Sun May 24 2020 Gayane Kazhoyan <kazhoyan@cs.uni-bremen.de> - 0.4.15-1
- Autogenerated by Bloom

* Sat May 23 2020 Gayane Kazhoyan <kazhoyan@cs.uni-bremen.de> - 0.4.14-3
- Autogenerated by Bloom

* Sat May 23 2020 Gayane Kazhoyan <kazhoyan@cs.uni-bremen.de> - 0.4.14-2
- Autogenerated by Bloom

* Sat May 23 2020 Gayane Kazhoyan <kazhoyan@cs.uni-bremen.de> - 0.4.14-1
- Autogenerated by Bloom

