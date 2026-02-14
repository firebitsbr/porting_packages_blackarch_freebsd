PORTNAME=	hexhttp
DISTVERSION=	v2.4.r1.g3d8b5c8
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Perform tests on HTTP headers and analyze the results to identify vulnerabilities and interesting behaviors.
WWW=		https://github.com/c0dejump/HExHTTP

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/# \
		??/https://github.com/c0dejump/HExHTTP/blob/main/requirements.txt \
		??/py-notify_py@${PY_FLAVOR} \
		??/py-urllib3@${PY_FLAVOR} \
		??/wafw00f \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
