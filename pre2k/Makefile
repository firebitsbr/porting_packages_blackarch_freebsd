PORTNAME=	pre2k
DISTVERSION=	24.ff51b3b
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Query for existence of pre-windows 2000 computer objects which can be leveraged to gain a foothold in a target domain.
WWW=		https://github.com/garrettfoster13/pre2k-TS

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/impacket-ba \
		??/py-ldap3@${PY_FLAVOR} \
		??/py-pyasn1@${PY_FLAVOR} \
		??/py-rich@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
