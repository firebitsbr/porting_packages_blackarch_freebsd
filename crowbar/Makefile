PORTNAME=	crowbar
DISTVERSION=	v4.2.r1.g4b563dc
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Brute forcing tool that can be used during penetration tests.
WWW=		https://github.com/galkan/crowbar

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/freerdp \
		??/openssh \
		??/openvpn \
		??/py-nmap@${PY_FLAVOR} \
		??/py-paramiko@${PY_FLAVOR} \
		??/tigervnc \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
