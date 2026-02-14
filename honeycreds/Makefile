PORTNAME=	honeycreds
DISTVERSION=	26.eaeb401
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Network credential injection to detect responder and other network poisoners.
WWW=		https://github.com/Ben0xA/HoneyCreds

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-cffi@${PY_FLAVOR} \
		??/py-smbprotocol@${PY_FLAVOR} \
		??/py-splunk-sdk@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
