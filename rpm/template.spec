Name:           ros-indigo-ros-emacs-utils
Version:        0.4.7
Release:        1%{?dist}
Summary:        ROS ros_emacs_utils package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-rosemacs
Requires:       ros-indigo-roslisp-repl
Requires:       ros-indigo-slime-ros
Requires:       ros-indigo-slime-wrapper
BuildRequires:  ros-indigo-catkin

%description
A metapackage of Emacs utils for ROS. Only there for simplifying the release
process.

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
* Mon Jun 01 2015 Gayane Kazhoyan <kazhoyan@cs.uni-bremen.de> - 0.4.7-1
- Autogenerated by Bloom

* Mon Jun 01 2015 Gayane Kazhoyan <kazhoyan@cs.uni-bremen.de> - 0.4.7-0
- Autogenerated by Bloom

* Thu Feb 12 2015 Gayane Kazhoyan <kazhoyan@cs.uni-bremen.de> - 0.4.6-0
- Autogenerated by Bloom

