PORTNAME=	silenttrinity
DISTVERSION=	293.08b1c61
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	An asynchronous, collaborative post-exploitation agent powered by Python and .NETs DLR.
WWW=		https://github.com/byt3bl33d3r/SILENTTRINITY

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/hypercorn \
		??/py-aiofiles@${PY_FLAVOR} \
		??/py-aiosqlite@${PY_FLAVOR} \
		??/py-aiowinreg@${PY_FLAVOR} \
		??/py-asciitree@${PY_FLAVOR} \
		??/py-asn1crypto@${PY_FLAVOR} \
		??/py-blinker@${PY_FLAVOR} \
		??/py-certifi@${PY_FLAVOR} \
		??/py-cffi@${PY_FLAVOR} \
		??/py-chardet@${PY_FLAVOR} \
		??/py-click@${PY_FLAVOR} \
		??/py-cryptography@${PY_FLAVOR} \
		??/py-defusedxml@${PY_FLAVOR} \
		??/py-dnslib@${PY_FLAVOR} \
		??/py-docopt@${PY_FLAVOR} \
		??/py-h11@${PY_FLAVOR} \
		??/py-h2@${PY_FLAVOR} \
		??/py-hpack@${PY_FLAVOR} \
		??/py-hyperframe@${PY_FLAVOR} \
		??/py-idna@${PY_FLAVOR} \
		??/py-itsdangerous@${PY_FLAVOR} \
		??/py-jinja@${PY_FLAVOR} \
		??/py-ldap3@${PY_FLAVOR} \
		??/py-markupsafe@${PY_FLAVOR} \
		??/py-minidump@${PY_FLAVOR} \
		??/py-minikerberos@${PY_FLAVOR} \
		??/py-msldap@${PY_FLAVOR} \
		??/py-multidict@${PY_FLAVOR} \
		??/py-netifaces@${PY_FLAVOR} \
		??/py-prompt_toolkit@${PY_FLAVOR} \
		??/py-pyasn1@${PY_FLAVOR} \
		??/py-pycparser@${PY_FLAVOR} \
		??/py-pypykatz@${PY_FLAVOR} \
		??/py-pytoml@${PY_FLAVOR} \
		??/py-quart@${PY_FLAVOR} \
		??/py-socks5line@${PY_FLAVOR} \
		??/py-sortedcontainers@${PY_FLAVOR} \
		??/py-termcolor@${PY_FLAVOR} \
		??/py-terminaltables@${PY_FLAVOR} \
		??/py-typing_extensions@${PY_FLAVOR} \
		??/py-urllib3@${PY_FLAVOR} \
		??/py-wcwidth@${PY_FLAVOR} \
		??/py-websockets@${PY_FLAVOR} \
		??/py-winsspi@${PY_FLAVOR} \
		??/py-wsproto@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
