PORTNAME=	infection-monkey
DISTVERSION=	v2.2.0.r3599.ga55fc8d
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Automated security testing tool for networks.
WWW=		https://github.com/guardicore/monkey

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/aws-cli \
		??/impacket \
		??/py-boto3@${PY_FLAVOR} \
		??/py-botocore@${PY_FLAVOR} \
		??/py-cffi@${PY_FLAVOR} \
		??/py-cryptography@${PY_FLAVOR} \
		??/py-dateutil@${PY_FLAVOR} \
		??/py-dpath@${PY_FLAVOR} \
		??/py-ecdsa@${PY_FLAVOR} \
		??/py-egg-timer@${PY_FLAVOR} \
		??/py-flask-jwt-extended@${PY_FLAVOR} \
		??/py-flask-pymongo@${PY_FLAVOR} \
		??/py-flask-restful@${PY_FLAVOR} \
		??/py-flask@${PY_FLAVOR} \
		??/py-gevent@${PY_FLAVOR} \
		??/py-jsonschema@${PY_FLAVOR} \
		??/py-ldaptor@${PY_FLAVOR} \
		??/py-marshmallow-enum@${PY_FLAVOR} \
		??/py-marshmallow@${PY_FLAVOR} \
		??/py-mongoengine@${PY_FLAVOR} \
		??/py-mongomock@${PY_FLAVOR} \
		??/py-netifaces@${PY_FLAVOR} \
		??/py-odict@${PY_FLAVOR} \
		??/py-paramiko@${PY_FLAVOR} \
		??/py-psutil@${PY_FLAVOR} \
		??/py-pycryptodome@${PY_FLAVOR} \
		??/py-pyftpdlib@${PY_FLAVOR} \
		??/py-pyjwt@${PY_FLAVOR} \
		??/py-pymssql@${PY_FLAVOR} \
		??/py-pypsrp@${PY_FLAVOR} \
		??/py-pypubsub@${PY_FLAVOR} \
		??/py-pypykatz@${PY_FLAVOR} \
		??/py-pysmb@${PY_FLAVOR} \
		??/py-pyspnego@${PY_FLAVOR} \
		??/py-pytest@${PY_FLAVOR} \
		??/py-requests-mock@${PY_FLAVOR} \
		??/py-ring@${PY_FLAVOR} \
		??/py-semver@${PY_FLAVOR} \
		??/py-serpentarium@${PY_FLAVOR} \
		??/py-simplejson@${PY_FLAVOR} \
		??/py-stix2-patterns@${PY_FLAVOR} \
		??/py-stix2@${PY_FLAVOR} \
		??/py-tqdm@${PY_FLAVOR} \
		??/py-urllib3@${PY_FLAVOR} \
		??/py-virtualenv@${PY_FLAVOR} \
		??/py-werkzeug@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		??/pyinstaller \
		??/pymssql \
		devel/py-six@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
