PORTNAME=	adidnsdump
DISTVERSION=	v1.4.0.r1.g95adaf8
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Active Directory Integrated DNS dumping by any authenticated user.
WWW=		https://github.com/dirkjanm/adidnsdump

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/impacket \
		??/py-dnspython@${PY_FLAVOR} \
		??/py-future@${PY_FLAVOR} \
		??/py-ldap3@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
