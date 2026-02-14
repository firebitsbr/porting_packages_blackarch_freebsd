PORTNAME=	reptor
DISTVERSION=	0.7
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	CLI tool to automate pentest reporting with SysReptor.
WWW=		https://github.com/Syslifters/reptor

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		devel/py-pip@${PY_FLAVOR}

RUN_DEPENDS=	??/py-asgiref@${PY_FLAVOR} \
		??/py-certifi@${PY_FLAVOR} \
		??/py-charset-normalizer@${PY_FLAVOR} \
		??/py-cvss@${PY_FLAVOR} \
		??/py-django@${PY_FLAVOR} \
		??/py-idna@${PY_FLAVOR} \
		??/py-markdown-it-py@${PY_FLAVOR} \
		??/py-mdurl@${PY_FLAVOR} \
		??/py-pyaml@${PY_FLAVOR} \
		??/py-pygments@${PY_FLAVOR} \
		??/py-rich@${PY_FLAVOR} \
		??/py-sqlparse@${PY_FLAVOR} \
		??/py-termcolor@${PY_FLAVOR} \
		??/py-tomli-w@${PY_FLAVOR} \
		??/py-tomli@${PY_FLAVOR} \
		??/py-urllib3@${PY_FLAVOR} \
		??/py-xmltodict@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
