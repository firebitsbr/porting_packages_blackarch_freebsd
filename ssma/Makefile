PORTNAME=	ssma
DISTVERSION=	215.2a2b6bd
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Simple Static Malware Analyzer.
WWW=		https://github.com/secrary/SSMA

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-elasticsearch@${PY_FLAVOR} \
		??/py-gitpython@${PY_FLAVOR} \
		??/py-magic@${PY_FLAVOR} \
		??/py-pefile@${PY_FLAVOR} \
		??/py-pyelftools@${PY_FLAVOR} \
		??/py-virustotal-api@${PY_FLAVOR} \
		??/py-yara-dex@${PY_FLAVOR} \
		??/ssdeep \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
