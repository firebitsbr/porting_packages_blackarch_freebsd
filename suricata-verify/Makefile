PORTNAME=	suricata-verify
DISTVERSION=	suricata.7.0.14.r41.g47e8ab8
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Suricata Verification Tests - Testing Suricata Output.
WWW=		https://github.com/OISF/suricata-verify

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/jq \
		??/py-future@${PY_FLAVOR} \
		??/py-yaml@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
