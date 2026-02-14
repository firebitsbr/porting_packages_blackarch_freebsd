PORTNAME=	dirsearch
DISTVERSION=	2607.19611c0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	HTTP(S) directory/file brute forcer.
WWW=		https://github.com/maurosoria/dirsearch

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-colorama@${PY_FLAVOR} \
		??/py-defusedcsv@${PY_FLAVOR} \
		??/py-defusedxml@${PY_FLAVOR} \
		??/py-httpx-ntlm@${PY_FLAVOR} \
		??/py-httpx@${PY_FLAVOR} \
		??/py-jinja@${PY_FLAVOR} \
		??/py-mysql-connector@${PY_FLAVOR} \
		??/py-ntlm-auth@${PY_FLAVOR} \
		??/py-psycopg@${PY_FLAVOR} \
		??/py-pyopenssl@${PY_FLAVOR} \
		??/py-pysocks@${PY_FLAVOR} \
		??/py-requests-ntlm@${PY_FLAVOR} \
		??/py-requests-toolbelt@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
