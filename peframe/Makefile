PORTNAME=	peframe
DISTVERSION=	135.70683b6
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Tool to perform static analysis on (portable executable) malware.
WWW=		https://github.com/guelfoweb/peframe

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-m2crypto@${PY_FLAVOR} \
		??/py-magic@${PY_FLAVOR} \
		??/py-msoffcrypto-tool@${PY_FLAVOR} \
		??/py-oletools@${PY_FLAVOR} \
		??/py-parameterized@${PY_FLAVOR} \
		??/py-pefile@${PY_FLAVOR} \
		??/py-virustotal-api@${PY_FLAVOR} \
		??/py-yara-dex@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
