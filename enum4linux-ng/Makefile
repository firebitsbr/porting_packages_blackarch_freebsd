PORTNAME=	enum4linux-ng
DISTVERSION=	444.0874859
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A next generation version of enum4linux.
WWW=		https://github.com/cddmp/enum4linux-ng

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/impacket \
		??/py-ldap3@${PY_FLAVOR} \
		??/py-yaml@${PY_FLAVOR} \
		??/smbclient \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
