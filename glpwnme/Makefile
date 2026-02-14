PORTNAME=	glpwnme
DISTVERSION=	21.aead58f
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	GLPI vulnerabilities checking tool.
WWW=		https://github.com/Orange-Cyberdefense/glpwnme

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		??/py-installer@${PY_FLAVOR} \
		??/py-poetry-core@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-bs4@${PY_FLAVOR} \
		??/py-certifi@${PY_FLAVOR} \
		??/py-charset-normalizer@${PY_FLAVOR} \
		??/py-idna@${PY_FLAVOR} \
		??/py-markdown-it-py@${PY_FLAVOR} \
		??/py-mdurl@${PY_FLAVOR} \
		??/py-packaging@${PY_FLAVOR} \
		??/py-pygments@${PY_FLAVOR} \
		??/py-rich@${PY_FLAVOR} \
		??/py-soupsieve@${PY_FLAVOR} \
		??/py-urllib3@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
