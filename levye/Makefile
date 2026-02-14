PORTNAME=	levye
DISTVERSION=	84.5406303
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A brute force tool which is support sshkey, vnckey, rdp, openvpn.
WWW=		https://github.com/galkan/levye

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/freerdp \
		??/openssh \
		??/openvpn \
		??/py-paramiko@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
