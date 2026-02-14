PORTNAME=	openssh-askpass
DISTVERSION=	2.1.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A plasma-like passphrase dialog for ssh.
WWW=		http://hugo.pereira.free.fr/software/index.php?page=package&package_list=software_list_qt4&package=openssh-askpass&full=0

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/cmake

RUN_DEPENDS=	??/openssh \
		??/qt5-svg \
		??/qt5-x11extras \
		??/xcb-util-keysyms


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
