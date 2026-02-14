PORTNAME=	wapiti
DISTVERSION=	3.2.10.r51.g2562893
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A vulnerability scanner for web applications.
WWW=		https://github.com/wapiti-scanner/wapiti

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-wheel@${PY_FLAVOR} \
		devel/git \
		devel/py-pip@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/mitmproxy \
		??/py-aiocache@${PY_FLAVOR} \
		??/py-aiosqlite@${PY_FLAVOR} \
		??/py-arsenic@${PY_FLAVOR} \
		??/py-async-timeout@${PY_FLAVOR} \
		??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-brotli@${PY_FLAVOR} \
		??/py-brotlicffi@${PY_FLAVOR} \
		??/py-browser-cookie3@${PY_FLAVOR} \
		??/py-cryptography@${PY_FLAVOR} \
		??/py-dnspython@${PY_FLAVOR} \
		??/py-h11@${PY_FLAVOR} \
		??/py-httpcore@${PY_FLAVOR} \
		??/py-httpx-ntlm@${PY_FLAVOR} \
		??/py-httpx-socks@${PY_FLAVOR} \
		??/py-httpx@${PY_FLAVOR} \
		??/py-humanize@${PY_FLAVOR} \
		??/py-importlib-metadata@${PY_FLAVOR} \
		??/py-keyring@${PY_FLAVOR} \
		??/py-loguru@${PY_FLAVOR} \
		??/py-mako@${PY_FLAVOR} \
		??/py-markupsafe@${PY_FLAVOR} \
		??/py-prance@${PY_FLAVOR} \
		??/py-pyasn1@${PY_FLAVOR} \
		??/py-pysocks@${PY_FLAVOR} \
		??/py-pyspnego@${PY_FLAVOR} \
		??/py-socksio@${PY_FLAVOR} \
		??/py-sqlalchemy@${PY_FLAVOR} \
		??/py-tld@${PY_FLAVOR} \
		??/py-wapiti-arsenic@${PY_FLAVOR} \
		??/py-wapiti-swagger@${PY_FLAVOR} \
		??/py-yaswfp@${PY_FLAVOR} \
		??/sslyze \
		devel/py-six@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
