PORTNAME=	balbuzard
DISTVERSION=	67.d6349ef1bc55
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A package of malware analysis tools in python to extract patterns of interest from suspicious files (IP addresses, domain names, known file headers, interesting strings, etc).
WWW=		https://bitbucket.org/decalage/balbuzard/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/mercurial \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-yara@${PY_FLAVOR} \
		??/yara \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
