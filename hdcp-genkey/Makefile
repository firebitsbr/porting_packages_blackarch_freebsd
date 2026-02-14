PORTNAME=	hdcp-genkey
DISTVERSION=	18.e8d342d
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Generate HDCP source and sink keys from the leaked master key.
WWW=		https://github.com/rjw57/hdcp-genkey

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-simplejson@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
