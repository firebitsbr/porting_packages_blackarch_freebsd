PORTNAME=	gmsadumper
DISTVERSION=	18.e03187c
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A tool that Reads any gMSA password blobs the user can access and parses the values.
WWW=		https://github.com/micahvandeusen/gMSADumper

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/impacket \
		??/py-ldap3@${PY_FLAVOR} \
		??/py-pycryptodomex@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
